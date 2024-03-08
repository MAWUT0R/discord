import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Resample the data on a quarterly basis and count the number of messages per quarter and per channel
quarterly_message_count = df.groupby('Channel').resample('Q').size().unstack(fill_value=0)

# Rename the columns to represent quarters
quarterly_message_count.columns = [f'{quarter.year} Q{quarter.quarter}' for quarter in quarterly_message_count.columns]

# Save the quarterly message count to a CSV file
quarterly_message_count.to_csv('quarterly_message_count.csv')

print("Quarterly message count grouped by channels saved to 'quarterly_message_count.csv'.")
