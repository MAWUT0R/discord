import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the day of the week and count the number of messages for each day
df['Day_of_Week'] = df['Date'].dt.dayofweek
activity_by_day = df.groupby('Day_of_Week').size().reset_index(name='Message_Count')

# Map day of the week to actual names
day_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
activity_by_day['Day_of_Week'] = activity_by_day['Day_of_Week'].map(day_mapping)

# Find the day with the highest message count
peak_day = activity_by_day.loc[activity_by_day['Message_Count'].idxmax()]

# Save the result to a CSV file
activity_by_day.to_csv('peak_user_activity_by_day.csv', index=False)

print("Peak user activity by day of the week saved to 'peak_user_activity_by_day.csv'.")
