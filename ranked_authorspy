import pandas as pd

# Load the cleaned Discord dataset
df = pd.read_csv('cleaned_discord.csv')

# Filter out bot authors
non_bot_df = df[df['Author'].str.lower().str.contains('bot') == False]

# Group by author and count the number of messages
author_message_counts = non_bot_df['Author'].value_counts().reset_index()
author_message_counts.columns = ['Author', 'Message Count']

# Rank the authors by message count
ranked_authors = author_message_counts.sort_values(by='Message Count', ascending=False)

# Save the ranked authors to a CSV file
ranked_authors.to_csv('ranked_authors.csv', index=False)

print("Ranked authors saved to 'ranked_authors.csv'.")
