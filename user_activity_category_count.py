import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Calculate the character count and content length for each message
df['Character_Count'] = df['Content'].str.len()
df['Content_Length'] = df['Content'].str.split().str.len()

# Group by Author and calculate activity metrics
user_activity = df.groupby('Author').agg({
    'Content': 'count',            # Count the number of messages per user
    'Character_Count': 'sum',      # Sum the character count of all messages per user
    'Content_Length': 'mean'       # Calculate the average content length of messages per user
})

# Rename columns for clarity
user_activity.columns = ['Message_Count', 'Total_Characters', 'Average_Content_Length']

# Classify users based on activity
user_activity['Activity_Category'] = pd.cut(user_activity['Message_Count'],
                                           bins=[0, 10, 100, 500, 1000, float('inf')],
                                           labels=['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

# Get the count of users in each activity category
activity_counts = user_activity['Activity_Category'].value_counts().reset_index()
activity_counts.columns = ['Activity_Category', 'User_Count']

# Save the categorized user activity counts to a new CSV file
activity_counts.to_csv('user_activity_category_counts.csv', index=False)

print("User activity category counts saved to 'user_activity_category_counts.csv'.")
