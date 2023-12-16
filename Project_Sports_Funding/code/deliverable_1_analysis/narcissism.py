#%%
import pandas as pd
import numpy as np
import os
import nltk
import re
import string
import sklearn
from nltk import regexp_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer

import matplotlib.pyplot as plt
stop_words = set(stopwords.words("english"))


#%%
def remove_noise_sent(tokenized_sent):
    filtered_sent=[]
    for w in tokenized_sent:
        if re.match('^[0-9]', w):
            continue
        else:
            if w not in stop_words:
                filtered_sent.append(w)
    return filtered_sent

def return_cleanedtext(tokenized_sent):
    return " ".join(tokenized_sent)

def remove_noise_lower(sent):
    sent = str(sent)
    for ch in ['\\', '`', '+', '*', '&', '-', '_', '!', '>', '<', '?', '$', '.', ';', '\"', ':']:
        if ch in sent:
            sent = sent.replace(ch, " ")
    sent = sent.replace(",", " ")
    sent = sent.translate(string.punctuation)
    sent = sent.lower()
    return sent

def tokenize_advanced_1(sent):
    pattern = r'''(?x) | (?:[A-Z]\.) | \w+(?:-\w+)* | \$?\d+(?:\.\d+)?%? | \.\.\. | [][.,;"'?():-_`] '''
    return nltk.regexp_tokenize(sent, pattern)

def tokenize_advanced_2(sent):
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    return tokenizer.tokenize(sent)

def tokenize_stemmed_1(sent):
    words = word_tokenize(sent)
    porter = PorterStemmer()
    tokenized_sent = []
    for w in words:
        if w not in non_stemmed_word_list:
            root_word = porter.stem(w)
        else :
            root_word = w
        tokenized_sent.append(root_word)
    return tokenized_sent


#%%
# Keep the current working directory as the Github folder for the entire project, not just the code folder
cwd = os.getcwd()
cwd = cwd.replace("/code", "")

df = pd.read_csv("{}/data/clean_data/final_data_merged.csv".format(cwd))
narcissism_wordlist_df = pd.read_csv("{}/data/narcissism_words_lists.csv".format(cwd))
#%%
# Cleaning and tokenizing stories
df['Story'] = df['Story'].apply(remove_noise_lower)
df['StoryCleaned'] = ''
df['Wordcount'] = ''
for i in range(0, df.shape[0]):
    tokenized_sent = remove_noise_sent(tokenize_advanced_2(df['Story'].iloc[i]))
    
    df['Wordcount'].iloc[i] = len(tokenized_sent)
    df['StoryCleaned'].iloc[i] = return_cleanedtext(tokenized_sent)

df.to_csv("{}/data/clean_data/final_data_merged_storycleaned.csv".format(cwd))

#%%
df.shape
#%%
# Create raw word counts for each of the words in the vocabulary in each of the dimensions in the Narcissism
for dimension in ['authority', 'superiority', 'exhibitionism', 'vanity', 'selfsufficiency', 'entitlement', 'exploitativeness']:
    phrases_list = narcissism_wordlist_df['{}'.format(dimension)].dropna().tolist()
    vectorizer = CountVectorizer(ngram_range = (1,2), vocabulary = list(set(phrases_list)))
    matrix = vectorizer.fit_transform(df.StoryCleaned)
    counts = pd.DataFrame(matrix.toarray(), index = df.CampaignURL, columns=vectorizer.get_feature_names_out())
    counts.to_csv("{}/data/narcissism_raw_data/{}_rawscores.csv".format(cwd,dimension))


#%%
df.dtypes
# %%
