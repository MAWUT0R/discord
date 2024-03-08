import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Resample the data on a weekly basis and count the number of messages per week
weekly_message_count = df['Channel'].resample('W').count()

# Create a DataFrame to store the weekly message count
weekly_message_count_df = pd.DataFrame(weekly_message_count)

# Rename the column to 'messages_count'
weekly_message_count_df.rename(columns={'Channel': 'messages_count'}, inplace=True)

# Add a 'week_start_date' column to represent the start date of each week
weekly_message_count_df['week_start_date'] = weekly_message_count_df.index - pd.to_timedelta(weekly_message_count_df.index.dayofweek, unit='D')

# Reorder the columns
weekly_message_count_df = weekly_message_count_df[['week_start_date', 'messages_count']]

# Save the weekly message count to a CSV file
weekly_message_count_df.to_csv('weekly_message_count.csv', index=False)

print("Weekly message count saved to 'weekly_message_count.csv'.")
