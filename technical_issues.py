import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import numpy as np

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Fill NaN values with empty strings
df['Content'] = df['Content'].fillna('')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Define a function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Preprocess and tokenize messages
all_messages = ' '.join(df['Content'].astype(str))  # Convert to string and join
tokenized_messages = preprocess_text(all_messages)

# Define technical keywords
technical_keywords = ['error', 'issue', 'bug', 'problem', 'crash', 'not working', 'technical']

# Find technical issues
technical_issues = [word for word in tokenized_messages if word in technical_keywords]

# Count the occurrences of each technical issue
technical_issue_counts = Counter(technical_issues)

# Convert to DataFrame
technical_issue_df = pd.DataFrame(list(technical_issue_counts.items()), columns=['Technical_Issue', 'Frequency'])

# Sort by frequency
technical_issue_df = technical_issue_df.sort_values(by='Frequency', ascending=False)

# Output to CSV
technical_issue_df.to_csv('technical_issues.csv', index=False)

print("Technical issues categorized and saved to 'technical_issues.csv'.")
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import numpy as np

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Fill NaN values with empty strings
df['Content'] = df['Content'].fillna('')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Define a function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Preprocess and tokenize messages
all_messages = ' '.join(df['Content'].astype(str))  # Convert to string and join
tokenized_messages = preprocess_text(all_messages)

# Define technical keywords
technical_keywords = ['error', 'issue', 'bug', 'problem', 'crash', 'not working', 'technical']

# Find technical issues
technical_issues = [word for word in tokenized_messages if word in technical_keywords]

# Count the occurrences of each technical issue
technical_issue_counts = Counter(technical_issues)

# Convert to DataFrame
technical_issue_df = pd.DataFrame(list(technical_issue_counts.items()), columns=['Technical_Issue', 'Frequency'])

# Sort by frequency
technical_issue_df = technical_issue_df.sort_values(by='Frequency', ascending=False)

# Output to CSV
technical_issue_df.to_csv('technical_issues.csv', index=False)

print("Technical issues categorized and saved to 'technical_issues.csv'.")
