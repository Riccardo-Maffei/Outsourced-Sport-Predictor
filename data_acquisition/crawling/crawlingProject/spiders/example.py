import json
import scrapy

from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


def parse_team(response):
    team_name = response.meta['team_name']
    team_url = response.meta['team_url']

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    won_draw_lost_pie_charts = soup.find_all('pk-donut-chart')
    match_results = {}

    for won_draw_lost_pie_chart in won_draw_lost_pie_charts:
        scores = json.loads(won_draw_lost_pie_chart['series'])
        labels = json.loads(won_draw_lost_pie_chart['labels'])
        match_results = {label: score for label, score in zip(labels, scores)}

    numerical_stats = soup.find_all('pk-num-stat-item')
    team_stats = {}

    for numerical_stat in numerical_stats:
        stat_value = numerical_stat.find('div', {'slot': 'stat-value'}).text.strip()
        stat_label = numerical_stat.find('div', {'slot': 'stat-label'}).text.strip()

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

        pie_charts = soup.find_all('pk-donut-chart')

        for pie_chart in pie_charts:
            scores = json.loads(pie_chart['series'])
            labels = json.loads(pie_chart['labels'])

            for label, score in zip(labels, scores):
                stats[label] = score

        numerical_stats_source = soup.find_all('pk-num-stat-item')

        for numerical_stat in numerical_stats_source:
            stat_value = numerical_stat.find('div', {'slot': 'stat-value'}).text.strip()
            stat_label = numerical_stat.find('div', {'slot': 'stat-label'}).text.strip()

            if isinstance(stat_value, str):
                original_stat = stat_value

                if stat_value.__contains__('%'):
                    stat_value = float(stat_value.replace('%', '')) / 100

                elif stat_value.__contains__('/'):
                    values_to_divide = stat_value.split('/')

                    values_to_divide = [float(value) for value in values_to_divide]

                    stat_value = values_to_divide[0] / values_to_divide[1]

                print("Parsing " + str(original_stat) + " to " + str(float(stat_value)))

                stat_value = float(stat_value)

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

        for team in teams[:1]:
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
