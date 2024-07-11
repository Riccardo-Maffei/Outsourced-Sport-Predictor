import pandas as pd
import json
import re

PATH_TO_JSON = '../Code/Outdated/EURO_Scraping/crawlingProject/spiders/output.json'

PATH_TO_COMPLETE_CSV = 'DataTables/Complete Dataset.csv'
PATH_TO_FILTERED_CSV = 'DataTables/Filtered Dataset.csv'

# Load the data from the JSON file

with open(PATH_TO_JSON, 'r') as file:
    data = json.load(file)

# Convert the JSON data to a pandas DataFrame
df = pd.json_normalize(data)

df.to_csv(PATH_TO_COMPLETE_CSV, index=False)

# Define the regex pattern to filter the "Team Name" column
pattern = re.compile(r'.*/euro2024/.*')

filtered_df = df[df['URL'].str.contains(pattern)]

filtered_df.to_csv(PATH_TO_FILTERED_CSV, index=False)
