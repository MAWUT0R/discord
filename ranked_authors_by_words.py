import pandas as pd

# Load the cleaned Discord dataset
df = pd.read_csv('cleaned_discord.csv')

# Filter out bot authors
non_bot_df = df[df['Author'].str.lower().str.contains('bot') == False].copy()

# Calculate the number of words in each message
non_bot_df.loc[:, 'Word Count'] = non_bot_df['Content'].str.split().str.len()

# Group by author and sum the word counts
author_word_counts = non_bot_df.groupby('Author')['Word Count'].sum().reset_index()

# Rank the authors by word count
ranked_authors = author_word_counts.sort_values(by='Word Count', ascending=False)

# Save the ranked authors to a CSV file
ranked_authors.to_csv('ranked_authors_by_words.csv', index=False)

print("Ranked authors by words saved to 'ranked_authors_by_words.csv'.")
