import pandas as pd

# Read the cleaned Discord data from the CSV file
df = pd.read_csv('cleaned_discord.csv')

# Group the data by author and sum the reactions received by each author
author_reaction_counts = df.groupby('Author')['Reactions'].sum().reset_index()

# Sort the authors based on the total reactions received in descending order
ranked_authors = author_reaction_counts.sort_values(by='Reactions', ascending=False)

# Save the ranked authors with their reaction counts to a new CSV file
ranked_authors.to_csv('ranked_authors_by_reactions.csv', index=False)

print("Ranked authors by reactions saved to 'ranked_authors_by_reactions.csv'.")
