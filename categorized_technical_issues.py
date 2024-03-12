import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Identify Technical Issues
technical_issues = []
for message in df['Content']:
    # Check if the message is a valid string
    if isinstance(message, str):
        # Example: Identify technical issues based on specific keywords or patterns
        if 'error' in message.lower() or 'bug' in message.lower() or 'crash' in message.lower():
            technical_issues.append(message)

# Categorize Based on Context
categorized_issues = {'User-Related': 0, 'System-Related': 0, 'External-Factors': 0}
for issue in technical_issues:
    # Check if the issue is a valid string
    if isinstance(issue, str):
        # Example: Categorize based on keywords in the message
        if 'user' in issue.lower() or 'account' in issue.lower() or 'access' in issue.lower():
            categorized_issues['User-Related'] += 1
        elif 'server' in issue.lower() or 'database' in issue.lower() or 'network' in issue.lower():
            categorized_issues['System-Related'] += 1
        else:
            categorized_issues['External-Factors'] += 1

# Output the Results to CSV
output_data = [{'Category': category, 'Issue_Count': count} for category, count in categorized_issues.items()]
output_df = pd.DataFrame(output_data)
output_df.to_csv('categorized_technical_issues.csv', index=False)
print("Categorized technical issues saved to 'categorized_technical_issues.csv'.")