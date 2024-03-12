import pandas as pd

# Load the cleaned Discord dataset
discord_df = pd.read_csv('cleaned_discord.csv')
discord_df['Date'] = pd.to_datetime(discord_df['Date'])

# Calculate the count of active authors per day
active_authors_per_day = discord_df.groupby(discord_df['Date'].dt.date)['Author'].nunique().reset_index()
active_authors_per_day.columns = ['Date', 'Active_Authors']
active_authors_per_day['Date'] = pd.to_datetime(active_authors_per_day['Date'])

# Load the ocean price dataset
ocean_price_df = pd.read_csv('ocean_price.csv')
ocean_price_df['DATE'] = pd.to_datetime(ocean_price_df['DATE'], format='%Y-%m-%d %H:%M:%S.%f')

# Merge the active authors data with the ocean price dataset based on the date column
merged_df = pd.merge(active_authors_per_day, ocean_price_df, left_on='Date', right_on='DATE', how='inner')

# Calculate the correlation between the price of $OCEAN and the number of active authors
correlation = merged_df['AVG_PRICE_USD'].corr(merged_df['Active_Authors'])

# Save the correlation to a CSV file
correlation_df = pd.DataFrame({'Correlation': [correlation]})
correlation_df.to_csv('correlation_ocean_active_authors.csv', index=False)

print("Correlation between the price of $OCEAN and the number of active authors saved to 'correlation_ocean_active_authors.csv'.")
