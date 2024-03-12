import pandas as pd

# Load the cleaned Discord dataset
discord_df = pd.read_csv('cleaned_discord.csv')
discord_df['Date'] = pd.to_datetime(discord_df['Date'])

# Load the ocean price dataset
ocean_price_df = pd.read_csv('ocean_price.csv')
ocean_price_df['DATE'] = pd.to_datetime(ocean_price_df['DATE'], format='%Y-%m-%d %H:%M:%S.%f')

# Merge the two datasets based on the date column
merged_df = pd.merge(discord_df, ocean_price_df, left_on='Date', right_on='DATE', how='inner')

# Calculate the correlation between the price of $OCEAN and the number of messages
correlation = merged_df['AVG_PRICE_USD'].corr(merged_df['Channel'])

# Save the correlation to a CSV file
correlation_df = pd.DataFrame({'Correlation': [correlation]})
correlation_df.to_csv('correlation_ocean_messages.csv', index=False)

print("Correlation between the price of $OCEAN and the number of messages saved to 'correlation_ocean_messages.csv'.")
