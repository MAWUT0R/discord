import pandas as pd
from datetime import datetime
import re

# Load the dataset
df = pd.read_csv('discord.csv')

# Extract the Channel IDs from the Channel column
df['Channel'] = df['Channel'].str.extract(r'\[(\d+)\]')

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M %p')

# Clean the Content column
df['Content'] = df['Content'].str.replace(r'https?://\S+|www\.\S+', '', regex=True) # Remove URLs

# Clean the Attachments column
df['Attachments'] = df['Attachments'].apply(lambda x: 'Yes' if pd.notnull(x) and x != '' else 'No')

# Extract attachment type based on extension
def extract_attachment_type(attachment_url):
    if pd.notnull(attachment_url):
        match = re.search(r'\.(\w+)(\?|$)', attachment_url)
        if match:
            return match.group(1).upper()
    return None

df['Attachment_Type'] = df['Attachments'].apply(extract_attachment_type)

# Clean the Reactions column and count occurrences of each reaction
def count_reactions(reactions_string):
    if pd.notnull(reactions_string):
        reactions_list = re.findall(r'\((\d+)\)', reactions_string)
        if reactions_list:
            return sum(int(count) for count in reactions_list)
    return 0

df['Reactions'] = df['Reactions'].apply(count_reactions)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_discord.csv', index=False)

print("Cleaning completed. Cleaned data saved to 'cleaned_discord.csv'.")
