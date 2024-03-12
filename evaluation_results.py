# Load the cleaned dataset
df = pd.read_csv('cleaned_discord.csv')

# Drop rows with missing values in the 'Content' column
df = df.dropna(subset=['Content'])

# Filter out messages from 'Deleted User' as potential spam/scam
deleted_user_messages = df[df['Author'] == 'Deleted User']

# Filter out non-spam messages from other authors
non_deleted_user_messages = df[df['Author'] != 'Deleted User'].sample(len(deleted_user_messages))

# Combine spam and non-spam messages
spam_nonspam_data = pd.concat([deleted_user_messages, non_deleted_user_messages])

# Split data into features and labels
X = spam_nonspam_data['Content']
y = np.where(spam_nonspam_data['Author'] == 'Deleted User', 'spam', 'non-spam')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical vectors using TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_vec, y_train)

# Predictions on the test set
y_pred = rf_classifier.predict(X_test_vec)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, output_dict=True)

# Convert classification report to dataframe and save to CSV
classification_df = pd.DataFrame(classification_rep).transpose()
classification_df.to_csv('classification_report.csv')

print("Classification report saved to 'classification_report.csv'.")
