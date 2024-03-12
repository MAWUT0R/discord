import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Filter out bot authors
non_bot_df = df[df['Author'].apply(lambda x: 'bot' not in x.lower())]

# Group by author and count attachments
attachment_counts = non_bot_df.groupby('Author')['Attachments'].count().reset_index()

# Sort the authors by attachment count
ranked_authors_by_attachments = attachment_counts.sort_values(by='Attachments', ascending=False)

# Save the ranked authors to a CSV file
ranked_authors_by_attachments.to_csv('ranked_authors_by_attachments.csv', index=False)

print("Ranked authors by attachments saved to 'ranked_authors_by_attachments.csv'.")
