import pandas as pd

df = pd.read_csv("C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv")

df.dropna(subset=['date', 'date_of_birth'])

# Convert 'date' and 'date_of_birth' columns to datetime format
df['date'] = pd.to_datetime(df['date'])
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

# Calculate age
df['age'] = df.apply(lambda row: row['date'].year - row['date_of_birth'].year - ((row['date'].month, row['date'].day) < (row['date_of_birth'].month, row['date_of_birth'].day)), axis=1)

df.drop(columns=['date', 'date_of_birth'], inplace=True)

output_file = "C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv"

df.to_csv(output_file, index=False)
