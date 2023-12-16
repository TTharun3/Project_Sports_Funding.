#%%
import pandas as pd
import os
import matplotlib.pyplot as plt

#%%
wd = os.getcwd()
try:
    wd = wd.replace("/code", "")
except: 
    pass
os.chdir(wd)

df = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score.csv".format(os.getcwd()))
df = df[df['is_english'] == 1]

#%%
df['joy_sad'] = df.apply(lambda x: 'joy' if x['joy'] > x['sadness'] else 'sadness', axis=1)
df['pos_neg'] = df.apply(lambda x: 'positive' if x['positive'] > x['negative'] else 'negative', axis=1)
df['trust_fear'] = df.apply(lambda x: 'trust' if x['trust'] > x['fear'] else 'fear', axis=1)
#%%
df['joy_sad']
#%%
df['pos_neg']
#%%
df['trust_fear']
#%%
df.to_csv('E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv', index=False)
# %%
##joy_sad_percentage values per SportName
# Create a pivot table to calculate the percentage of joy_sad values per SportName
pt = pd.pivot_table(df, index='SportName', columns='joy_sad', values='CampaignURL', aggfunc='count', fill_value=0)
pt['joy_sad_percentage'] = pt['joy'] / (pt['joy'] + pt['sadness']) * 100

# Filter the pivot table to exclude SportName values with 100% joy_sad_percentage
pt_filtered = pt[pt['joy_sad_percentage'] < 100]

# Create a cumulative bar chart of the joy_sad_percentage values per SportName
ax = pt_filtered['joy_sad_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Joy and Sadness Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()
#%%
##pos_neg_percentage values per SportName
# Create a pivot table to calculate the percentage of pos_neg values per SportName
pt = pd.pivot_table(df, index='SportName', columns='pos_neg', values='CampaignURL', aggfunc='count', fill_value=0)
pt['pos_neg_percentage'] = pt['positive'] / (pt['positive'] + pt['negative']) * 100

# Filter the pivot table to only include sport names without 100% positive or negative scores
pt_filtered = pt[pt['pos_neg_percentage'] != 100]

# Create a cumulative bar chart of the pos_neg_percentage values per SportName
ax = pt_filtered['pos_neg_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Positive and Negative Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
##trust_fear_percentage values per SportName
# Create a pivot table to calculate the percentage of trust_fear values per SportName
pt = pd.pivot_table(df, index='SportName', columns='trust_fear', values='CampaignURL', aggfunc='count', fill_value=0)
pt['trust_fear_percentage'] = pt['trust'] / (pt['trust'] + pt['fear']) * 100

# Filter the pivot table to only include sport names without 100% trust or fear scores
pt_filtered = pt[pt['trust_fear_percentage'] != 100]

# Create a cumulative bar chart of the trust_fear_percentage values per SportName
ax = pt_filtered['trust_fear_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Trust and Fear Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
####joy_sad_percentage values per Country
# Create a pivot table to calculate the percentage of joy_sad values per SportName
pt = pd.pivot_table(df, index='Country', columns='joy_sad', values='CampaignURL', aggfunc='count', fill_value=0)
pt['joy_sad_percentage'] = pt['joy'] / (pt['joy'] + pt['sadness']) * 100

# Filter the pivot table to exclude SportName values with 100% joy_sad_percentage
pt_filtered = pt[pt['joy_sad_percentage'] < 100]

# Create a cumulative bar chart of the joy_sad_percentage values per SportName
ax = pt_filtered['joy_sad_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Joy and Sadness Scores per Country (Excluding 100%)')
plt.tight_layout()

plt.show()

#%%
##pos_neg_percentage values per Country
# Create a pivot table to calculate the percentage of pos_neg values per SportName
pt = pd.pivot_table(df, index='Country', columns='pos_neg', values='CampaignURL', aggfunc='count', fill_value=0)
pt['pos_neg_percentage'] = pt['positive'] / (pt['positive'] + pt['negative']) * 100

# Filter the pivot table to only include sport names without 100% positive or negative scores
pt_filtered = pt[pt['pos_neg_percentage'] != 100]

# Create a cumulative bar chart of the pos_neg_percentage values per SportName
ax = pt_filtered['pos_neg_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Positive and Negative Scores per Country (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
##trust_fear_percentage values per Country
# Create a pivot table to calculate the percentage of trust_fear values per SportName
pt = pd.pivot_table(df, index='Country', columns='trust_fear', values='CampaignURL', aggfunc='count', fill_value=0)
pt['trust_fear_percentage'] = pt['trust'] / (pt['trust'] + pt['fear']) * 100

# Filter the pivot table to only include sport names without 100% trust or fear scores
pt_filtered = pt[pt['trust_fear_percentage'] != 100]

# Create a cumulative bar chart of the trust_fear_percentage values per SportName
ax = pt_filtered['trust_fear_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Trust and Fear Scores per Country (Excluding 100%)')
plt.tight_layout()
plt.show()


# %%
import matplotlib.pyplot as plt

# count the occurrences of each category in the 'joy_sad' column
counts = df['joy_sad'].value_counts()

# create a bar plot of the counts
plt.bar(counts.index, counts.values)

# add axis labels and a title
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Counts of Joy and Sadness in Joy-Sadness Column')

# display the plot
plt.show()

# %%
import matplotlib.pyplot as plt

# count the occurrences of each category in the 'pos_neg' column
counts = df['pos_neg'].value_counts()

# create a bar plot of the counts
plt.bar(counts.index, counts.values)

# add axis labels and a title
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Counts of pos_neg in pos_neg Column')

# display the plot
plt.show()
# %%
import matplotlib.pyplot as plt

# count the occurrences of each category in the 'trust_fear' column
counts = df['trust_fear'].value_counts()

# create a bar plot of the counts
plt.bar(counts.index, counts.values)

# add axis labels and a title
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Counts of trust_fear in trust_fear Column')

# display the plot
plt.show()



#### Sentimnet Classification


# Joy and Sadness
# %%
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE
# Load the data
data = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv')
#%%
# Extract the input features and labels
features = data['StoryCleaned']
labels = data['joy_sad']
#%%
# Define the stop words
stop = ['a', 'an', 'the', 'and', 'but', 'or', 'if', 'because', 'as', 'what', 'which', 'this', 'that', 'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both', 'through', 'about', 'for', 'is', 'of', 'while', 'during', 'to', 'What', 'Which', 'Is', 'If', 'While', 'This']
# Vectorize the input features
vectorizer = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8, stop_words=stop)
processed_features = vectorizer.fit_transform(features).toarray()
#%%
# Handle class imbalance using SMOTE
smote = SMOTE(random_state=0)
processed_features, labels = smote.fit_resample(processed_features, labels)
#%%
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.3, random_state=0)
#%%
# Train a Random Forest Classifier on the training data
text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)
#%%
# Make predictions on the test data
predictions = text_classifier.predict(X_test)
#%%
# Evaluate the performance of the model using a confusion matrix
cm = confusion_matrix(y_test, predictions)
print(cm)

# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
print(classification_report(y_test,predictions))
# %%
print(accuracy_score(y_test, predictions))
# %%
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(text_classifier, X_test, y_test)


#Trust and Fear


#%%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE
#%%
# Load the data
data = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv')
#%%
# Extract the input features and labels
features = data['StoryCleaned']
labels = data['trust_fear']
#%%
# Vectorize the input features
vectorizer = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(features).toarray()
#%%
# Handle class imbalance using SMOTE
smote = SMOTE(random_state=0)
processed_features, labels = smote.fit_resample(processed_features, labels)
#%%
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.3, random_state=0)
#%%
# Train a Random Forest Classifier on the training data
text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)
#%%
# Make predictions on the test data
predictions = text_classifier.predict(X_test)
#%%
# Evaluate the performance of the model using a confusion matrix
cm = confusion_matrix(y_test, predictions)
print(cm)


# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
print(classification_report(y_test,predictions))
# %%
print(accuracy_score(y_test, predictions))
#%%
true_fear = 0
true_trust = 0
for i in range(len(predictions)):
    if predictions[i] == y_test.values[i]:
        if predictions[i] == 'fear':
            true_fear += 1
        else:
            true_trust += 1

print("Number of correctly identified instances for fear: ", true_fear)
print("Number of correctly identified instances for trust: ", true_trust)




# Positive and Negative



# %%
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load the data
data = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv')
#%%
# Extract the input features and labels
features = data['StoryCleaned']
labels = data['pos_neg']
#%%
# Define the stop words
stop = ['a', 'an', 'the', 'and', 'but', 'or', 'if', 'because', 'as', 'what', 'which', 'this', 'that', 'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both', 'through', 'about', 'for', 'is', 'of', 'while', 'during', 'to', 'What', 'Which', 'Is', 'If', 'While', 'This']
# Vectorize the input features
vectorizer = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8, stop_words=stop)
processed_features = vectorizer.fit_transform(features).toarray()
#%%
# Handle class imbalance using SMOTE
smote = SMOTE(random_state=0)
processed_features, labels = smote.fit_resample(processed_features, labels)
#%%
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.3, random_state=0)
#%%
# Train a Random Forest Classifier on the training data
text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)
#%%
# Make predictions on the test data
predictions = text_classifier.predict(X_test)
#%%
# Evaluate the performance of the model using a confusion matrix
cm = confusion_matrix(y_test, predictions)
print(cm)

# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
print(classification_report(y_test,predictions))
# %%
print(accuracy_score(y_test, predictions))
# %%
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(text_classifier, X_test, y_test)
# %%
