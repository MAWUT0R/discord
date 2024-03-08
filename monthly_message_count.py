import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Resample the data on a monthly basis and count the number of messages per month
monthly_message_count = df['Channel'].resample('M').count()

# Create a DataFrame to store the monthly message count
monthly_message_count_df = pd.DataFrame(monthly_message_count)

# Rename the column to 'messages_count'
monthly_message_count_df.rename(columns={'Channel': 'messages_count'}, inplace=True)

# Add a 'month_start_date' column to represent the start date of each month
monthly_message_count_df['month_start_date'] = monthly_message_count_df.index.to_period('M').to_timestamp()

# Reorder the columns
monthly_message_count_df = monthly_message_count_df[['month_start_date', 'messages_count']]

# Save the monthly message count to a CSV file
monthly_message_count_df.to_csv('monthly_message_count.csv', index=False)

print("Monthly message count saved to 'monthly_message_count.csv'.")
