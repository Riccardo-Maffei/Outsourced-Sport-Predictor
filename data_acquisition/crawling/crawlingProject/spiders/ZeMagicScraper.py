import json
import scrapy

from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


DEFAULT_HTML_LABEL_PROPERTIES = {'slot': 'stat-label'}
DEFAULT_HTML_VALUE_PROPERTIES = {'slot': 'stat-value'}


def scrape_pie_chart(soup,
                     pie_chart_html_name='pk-donut-chart',
                     primary_title_html_name='primary-text',
                     secondary_title_html_name='secondary-text',
                     labels_html_name='labels',
                     series_html_name='series'):
    pie_charts = soup.find_all(pie_chart_html_name)

    pie_chart_results = {}

    for pie_chart in pie_charts:
        # Extract attributes
        primary_text = pie_chart.get(primary_title_html_name)
        secondary_text = pie_chart.get(secondary_title_html_name)

        labels = json.loads(pie_chart[labels_html_name])
        series = json.loads(pie_chart[series_html_name])

        title = primary_text + " " + secondary_text

        pie_chart_results[title] = {label: serie for label, serie in zip(labels, series)}

    return pie_chart_results


def scrape_label_value_pair(soup,
                            html_label_tag='div',
                            html_value_tag='div',
                            html_label_properties=None,
                            html_value_properties=None):

    # Use the default values if none are provided
    if html_label_properties is None:
        html_label_properties = DEFAULT_HTML_LABEL_PROPERTIES
    if html_value_properties is None:
        html_value_properties = DEFAULT_HTML_VALUE_PROPERTIES

    stat_label = soup.find(html_label_tag, html_label_properties).text.strip()
    stat_value = soup.find(html_value_tag, html_value_properties).text.strip()

    if isinstance(stat_value, str):
        if stat_value.__contains__('%'):
            stat_value = float(stat_value.replace('%', '')) / 100

        elif stat_value.__contains__('/'):
            values_to_divide = stat_value.split('/')

            values_to_divide = [float(value) for value in values_to_divide]

            stat_value = values_to_divide[0] / values_to_divide[1]

        stat_value = float(stat_value)

    return stat_label, stat_value


def parse_team(response):
    team_name = response.meta['team_name']
    team_url = response.meta['team_url']

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Pie Chart Scraping
    match_results = scrape_pie_chart(soup)

    numerical_stats = soup.find_all('pk-num-stat-item')
    team_stats = {}

    for numerical_stat in numerical_stats:
        stat_label, stat_value = scrape_label_value_pair(numerical_stat)

        team_stats[stat_label] = stat_value

    stats_tab = soup.find_all('pk-tab', {'tab-id': 'stats'})

    team_stats_url = ""

    for stats_tab in stats_tab:
        team_stats_url = stats_tab.find('a')['href']

    full_stats_url = response.urljoin(team_stats_url)

    yield scrapy.Request(full_stats_url, callback=parse_team_advanced,
                         meta={'team_name': team_name,
                               'team_url': team_url,
                               'Match Results': match_results,
                               'Team statistics': team_stats
                               })


def parse_team_advanced(response):
    team_name = response.meta['team_name']
    team_url = response.meta['team_url']

    match_results = response.meta['Match Results']
    team_stats = response.meta['Team statistics']

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    stats_types = soup.find_all('pk-box')

    advanced_stats = {}

    for stats_type in stats_types:
        stat_title = stats_type.find('h2')
        stats = {}

        stats = {**stats, **scrape_pie_chart(stats_type)}

        numerical_stats_source = stats_type.find_all('pk-num-stat-item')

        for numerical_stat in numerical_stats_source:
            stat_label, stat_value = scrape_label_value_pair(numerical_stat)

            stats[stat_label] = stat_value

        advanced_stats[stat_title.text.strip()] = stats

    yield {
        'Team Name': team_name,
        'URL': team_url,
        'Match Overview': match_results,
        'Basic statistics': team_stats,
        'Advanced Statistics': advanced_stats
    }


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["uefa.com"]
    start_urls = ["https://www.uefa.com/euro2024/teams/"]

    def parse(self, response, **kwargs):
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        teams = soup.find_all('div', class_='team team-is-team')

        for team in teams:
            team_name = team.find('a', class_='team-wrap').text.strip()

            team_url = team.find('a')['href']
            full_team_url = response.urljoin(team_url)

            yield scrapy.Request(full_team_url, callback=parse_team,
                                 meta={'team_name': team_name, 'team_url': full_team_url})


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "output.json": {
                    "format": "json",
                    "overwrite": True,
                    "indent": 4,  # Pretty print with an indent of 4 spaces
                },
            },
        })

    process.crawl(ExampleSpider)
    process.start()  # the script will block here until the crawling is finished
