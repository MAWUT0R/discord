import pandas as pd

# Load the cleaned Discord dataset
df = pd.read_csv('cleaned_discord.csv')

# Filter out bot authors
non_bot_df = df[~df['Author'].str.lower().str.contains('bot')]

# Calculate the number of characters in each message
non_bot_df.loc[:, 'Character Count'] = non_bot_df['Content'].str.len()

# Group by author and sum the character counts
author_character_counts = non_bot_df.groupby('Author')['Character Count'].sum().reset_index()

# Rank the authors by character count
ranked_authors = author_character_counts.sort_values(by='Character Count', ascending=False)

# Save the ranked authors to a CSV file
ranked_authors.to_csv('ranked_authors_by_characters.csv', index=False)

print("Ranked authors by characters saved to 'ranked_authors_by_characters.csv'.")
