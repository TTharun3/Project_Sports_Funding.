#%%

pip install langdetect
from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
    except:
        lang = 'unknown'
    return lang
#%%

import pandas as pd
df = pd.read_csv(os.getcwd() + "/data/clean_data/final_dataset_analysis.csv")
#%%

# apply the detect_language function to the 'text' column
df['language'] = df['Story_Original'].apply(detect_language)

# create a new column with 1 for English and 0 for other languages
df['is_english'] = df['language'].apply(lambda x: 1 if x == 'en' else 0)
df.head()
#%%
df.to_csv('final_dataset_textanalysis.csv', index=False)
