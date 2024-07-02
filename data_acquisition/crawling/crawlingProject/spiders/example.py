import json
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["uefa.com"]
    start_urls = ["https://www.uefa.com/euro2024/teams/"]

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        teams = soup.find_all('div', class_='team team-is-team')

        for team in teams:
            team_name = team.find('a', class_='team-wrap').text.strip()

            team_url = team.find('a')['href']
            full_team_url = response.urljoin(team_url)

            yield scrapy.Request(full_team_url, callback=self.parse_team,
                                 meta={'team_name': team_name, 'team_url': full_team_url})

    def parse_team(self, response):
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
        team_stats = []

        for numerical_stat in numerical_stats:
            stat_value = numerical_stat.find('div', {'slot': 'stat-value'}).text.strip()
            stat_label = numerical_stat.find('div', {'slot': 'stat-label'}).text.strip()

            team_stats.append({stat_label: stat_value})

        yield {
            'Team Name': team_name,
            'URL': team_url,
            'Match Results': match_results,
            'Team statistics': team_stats
        }


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
