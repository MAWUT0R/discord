import pandas as pd
from datetime import datetime

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the total number of channels
total_channels = df['Channel'].nunique()

# Calculate the total number of authors
total_authors = df['Author'].nunique()

# Calculate the total number of words written in the content
total_words = df['Content'].str.split().str.len().sum()

# Calculate the total number of days the data spans
start_date = df['Date'].min()
end_date = df['Date'].max()
total_days = (end_date - start_date).days + 1

# Create a DataFrame to store the calculated metrics
metrics_data = {
    'Total Channels': [total_channels],
    'Total Authors': [total_authors],
    'Total Words': [total_words],
    'Total Days': [total_days]
}
metrics_df = pd.DataFrame(metrics_data)

# Save the metrics to a new CSV file
metrics_df.to_csv('discord_metrics.csv', index=False)

print("Metrics calculated and saved to 'discord_metrics.csv'.")
