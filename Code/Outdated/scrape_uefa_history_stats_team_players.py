from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup WebDriver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH_TO_CHROMEDRIVER = 'EURO_Scraping/chromedriver-win64/chromedriver.exe'

service = Service(PATH_TO_CHROMEDRIVER)

driver = webdriver.Chrome(service=service, options=options)

# Define the base parts of the URL
url_start = "https://www.uefa.com/uefaeuro/history/seasons/"
years = [str(year) for year in range(2020, 1999, -4)]
statistics_parts = ["statistics/"]
entities = ["players/"]  # , "teams/"]
categories = ["goalkeeping/", "disciplinary/"]
# "", "goals/", "attempts/","distribution/", "attacking/", "defending/",


# Initialize an empty list to store all possible URLs
base_urls = []

# Create nested loops to generate all combinations
for year in years:
    for stat in statistics_parts:
        for entity in entities:
            for category in categories:
                url = f"{url_start}{year}/{stat}{entity}{category}"
                base_urls.append(url)


# Function to scroll the page to load more data
def scroll_to_load(driver, scroll_pause_time=0.4):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Function to scrape data from a URL and save it to a CSV file
def scrape_data(url):
    try:
        driver.get(url)

        # Increase wait time and ensure correct element is targeted
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'statistics-detail'))
        )

        # Scroll to the bottom of the page to load all data
        scroll_to_load(driver)

        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the table within the statistics-detail class
        table = soup.find('div', class_='statistics-detail')
        if not table:
            print(f"Table not found for URL: {url}")
            return

        # Extract data from the table
        rows = table.select(".ag-row")
        table_data = []
        rank_identifier_data = []
        goals_data = []

        # First pass to extract rank and identifier
        for row in rows:
            row_data = {}
            cells = row.find_all('div', role='gridcell')
            for cell in cells:
                col_id = cell.get('col-id')
                cell_value = cell.find('span', class_='ag-cell-value').text.strip()
                row_data[col_id] = cell_value

            if 'rank' in row_data and 'identifier' in row_data:
                rank_identifier_data.append(row_data)
            else:
                goals_data.append(row_data)

        # Ensure both lists are of the same length
        if len(rank_identifier_data) != len(goals_data):
            print(f"Mismatch between number of teams and number of statistics rows for URL: {url}")
            return

        # Combine the data
        for i in range(len(rank_identifier_data)):
            combined_data = {**rank_identifier_data[i], **goals_data[i], 'url': url}
            table_data.append(combined_data)

        # Create a DataFrame from the data
        df = pd.DataFrame(table_data)

        # Determine the filename from the URL
        year = url.split('/')
        filename = f'C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\mycode\\output\\uefa_team_stats_{year[-1]}_{year[-2]}_{year[-3]}_{year[-4]}_{year[-5]}.csv'

        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")


# Iterate through the list of URLs and scrape data for each
for base_url in base_urls:
    scrape_data(base_url)

driver.quit()
