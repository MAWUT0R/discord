import pandas as pd

# Load the cleaned Discord dataset
discord_df = pd.read_csv('cleaned_discord.csv')
discord_df['Date'] = pd.to_datetime(discord_df['Date'])

# Group by author and find the minimum date each author posted
first_post_dates = discord_df.groupby('Author')['Date'].min().reset_index()

# Calculate the count of new authors per day
new_authors_per_day = first_post_dates.groupby(first_post_dates['Date'].dt.date).size().reset_index()
new_authors_per_day.columns = ['Date', 'New_Authors']
new_authors_per_day['Date'] = pd.to_datetime(new_authors_per_day['Date'])

# Load the ocean price dataset
ocean_price_df = pd.read_csv('ocean_price.csv')
ocean_price_df['DATE'] = pd.to_datetime(ocean_price_df['DATE'], format='%Y-%m-%d %H:%M:%S.%f')

# Merge the new authors data with the ocean price dataset based on the date column
merged_df = pd.merge(new_authors_per_day, ocean_price_df, left_on='Date', right_on='DATE', how='inner')

# Calculate the correlation between the price of $OCEAN and the number of new authors
correlation = merged_df['AVG_PRICE_USD'].corr(merged_df['New_Authors'])

# Save the correlation to a CSV file
correlation_df = pd.DataFrame({'Correlation': [correlation]})
correlation_df.to_csv('correlation_ocean_new_authors.csv', index=False)

print("Correlation between the price of $OCEAN and the number of new authors saved to 'correlation_ocean_new_authors.csv'.")
