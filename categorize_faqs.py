import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure stopwords and punkt resources are downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Load the cleaned Discord dataset
discord_df = pd.read_csv('cleaned_discord.csv')

# Preprocess the data
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())
    # Remove stopwords and non-alphabetic characters
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered_tokens

# Identify frequently asked questions
all_questions = ' '.join(discord_df['Content'].dropna())
tokenized_questions = preprocess_text(all_questions)
faq_counter = Counter(tokenized_questions)

# Define themes for categorization
themes = {
    'technical': ['technical', 'code', 'development', 'api', 'integration', 'network'],
    'price-related': ['price', 'market', 'valuation', 'exchange'],
    'general information': ['information', 'faq', 'community', 'documentation']
}

# Categorize FAQs
categorized_faqs = {theme: {} for theme in themes.keys()}

for word, count in faq_counter.items():
    for theme, keywords in themes.items():
        if any(keyword in word for keyword in keywords):
            categorized_faqs[theme][word] = count

# Sort categorized FAQs by count
for theme, faqs in categorized_faqs.items():
    categorized_faqs[theme] = dict(sorted(faqs.items(), key=lambda item: item[1], reverse=True))

# Output the results to a new CSV file
output_data = {'Theme': [], 'Question': [], 'Count': []}
for theme, faqs in categorized_faqs.items():
    for word, count in faqs.items():
        output_data['Theme'].append(theme)
        output_data['Question'].append(word)
        output_data['Count'].append(count)

output_df = pd.DataFrame(output_data)
output_df.to_csv('categorized_faqs.csv', index=False)

print("Categorized FAQs saved to 'categorized_faqs.csv'.")
