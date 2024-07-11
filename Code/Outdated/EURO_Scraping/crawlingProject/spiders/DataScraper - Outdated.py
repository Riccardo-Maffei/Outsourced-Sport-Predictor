from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Path to the chromedriver executable
chrome_driver_path = r'../../../../../chromedriver-win64/chromedriver.exe'

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# URL of the page to scrape
url = 'https://www.uefa.com/euro2024/teams/'

# Fetch the webpage content
driver.get(url)
html = driver.page_source

# Parse the content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the relevant data
# Adjust the selectors according to the actual structure of the webpage
teams = soup.find_all('div', class_='team team-is-team')  # Example class name

team_data = []
for team in teams:
    team_name = team.find('a', class_='team-wrap').text.strip()
    team_url = team.find('a')['href']
    team_data.append({'Team Name': team_name, 'URL': team_url})

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(team_data)
df.to_csv('euro2024_teams.csv', index=False)

print("Data saved to euro2024_teams.csv")

# Close the Selenium WebDriver
driver.quit()
