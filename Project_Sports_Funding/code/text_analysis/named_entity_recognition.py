# %%
import pandas as pd
import spacy
# %%
# load spaCy's English model
nlp = spacy.load('en_core_web_sm')

# read the CSV file containing the text data
# %%
import os
cwd = os.getcwd()
cwd = cwd.replace("\\code\\text_analysis", "")
cwd
# %%
df = pd.read_csv("{}\\data\\clean_data\\final_dataset_textanalysis_sentiment_score.csv".format(cwd))
# %%

# filter for English language stories
english_df = df[df['is_english'] == 1].copy()
english_df.columns
# %%
# create columns to store named entity recognition results
entities = ['PERSON', 'ORG', 'PRODUCT', 'EVENT', 'MONEY', 'DATE', 'TIME', 'GPE', 'LOC', 'NORP']
for entity in entities:
    english_df[f'{entity}_Entity'] = ''

# loop through each story and perform named entity recognition using spaCy
for i, story in english_df['Story_Original'].iteritems():
    doc = nlp(story)
    for ent in doc.ents:
        if ent.label_ in ['PERSON']:
            english_df.at[i, 'PERSON_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['ORG']:
            english_df.at[i, 'ORG_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['PRODUCT']:
            english_df.at[i, 'PRODUCT_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['EVENT']:
            english_df.at[i, 'EVENT_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['MONEY']:
            english_df.at[i, 'MONEY_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['DATE']:
            english_df.at[i, 'DATE_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['TIME']:
            english_df.at[i, 'TIME_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['GPE', 'LOC','FAC']:
            english_df.at[i, 'LOC_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['NORP']:
            english_df.at[i, 'NORP_Entity'] += f"{ent.text} ({ent.label_}), "
# %%
english_df.columns
# %%

df2 = english_df.filter(['CampaignURL','SportName','City','State','Country','TeamOrAthlete','language','FundsRaisedPercent','PERSON_Entity', 'ORG_Entity','PRODUCT_Entity', 'EVENT_Entity', 'MONEY_Entity', 'DATE_Entity','TIME_Entity', 'GPE_Entity', 'LOC_Entity', 'NORP_Entity'], axis=1)
print(df2)

#%%

# success column
# create function to map moneyraised tobinary values
def map_success(FundsRaisedPercent):
    if FundsRaisedPercent >= 100:
        return 1
    else:
        return 0

# apply function to create new column
df2['IsSuccess'] = df2['FundsRaisedPercent'].apply(map_success)

#%%
pd.set_option('display.max_columns', None)
df2.head

# %%
# write the results to a new CSV file
df2.to_csv("{}\\data\\text_analysis_data\\ner_results.csv".format(cwd))


# %%

import spacy
from spacy import displacy
import pandas as pd
# %%
# load spaCy's English model
nlp = spacy.load('en_core_web_sm')
# %%
# read the CSV file containing the text data
df = english_df
# %%
# choose a story to visualize the named entities
CampaignURL = "https://sportfunder.com/hunterpowershowcase/28192"
row_index = df.loc[df['CampaignURL'] == CampaignURL].index[0] # find the row index of the specified CampaignURL
story_text = df.loc[row_index, 'Story_Original']

# perform named entity recognition using spaCy
doc = nlp(story_text)
# %%#
# visualize the named entities using displacy
displacy.render(doc, style='ent', jupyter=True)

# %%
import matplotlib.pyplot as plt
import pandas as pd
# %%
df = df2
import matplotlib.pyplot as plt

# Assuming that the data is stored in a dataframe called df



# create a list of the columns to analyze
cols_to_analyze = ['PERSON_Entity', 'ORG_Entity', 'PRODUCT_Entity'	,'EVENT_Entity'	,'MONEY_Entity'	,'DATE_Entity'	,'TIME_Entity'	,'LOC_Entity'	,'NORP_Entity']

# create a dataframe to store the results
results_df = pd.DataFrame(columns=['Column', 'Empty%', 'Not Empty%'])

# calculate the percentages and store them in the results dataframe
for col in cols_to_analyze:
    empty_count = df[col].isnull().sum() + df[col].eq('').sum()
    empty_percent = empty_count / len(df) * 100
    not_empty_percent = (len(df) - empty_count) / len(df) * 100
    results_df = results_df.append({'Column': col, 'Empty%': empty_percent, 'Not Empty%': not_empty_percent}, ignore_index=True)

# create a bar chart to visualize the results
plt.bar(results_df['Column'], results_df['Not Empty%'], color='#008080', label='No Entity %', edgecolor='white', width=0.8)
plt.bar(results_df['Column'], results_df['Empty%'], color='#FA8072', label='Extracted Entity %', edgecolor='white', width=0.8, bottom=results_df['Not Empty%'])
plt.xlabel('Named Entities')
plt.ylabel('Percentage of Stories Mentioning Each Entity')
plt.title('Mention of Entities in Stories')
plt.xticks(rotation=90)  # Rotating x-axis labels by 90 degrees for better readability

# Adding percentage labels above the bars
#for i, value in enumerate(results_df['Empty%']):
    #plt.text(i, 50+value/2, f"{value:.1f}%", ha='center', fontsize=8, color='black')
for i, value in enumerate(results_df['Not Empty%']):
    plt.text(i, value/2, f"{value:.1f}%", ha='center',va='center', fontsize=8, color='black')

plt.legend()
plt.show()



# %%

#Finding top 5  entities


# Read the dataset into a pandas dataframe
df = english_df
# %%
# Combine all the records in the "Story_Original" column into a single string
combined_text = ' '.join(df['Story_Original'].astype(str))
# %%
# Perform Named Entity Recognition (NER) on the combined text
nlp.max_length = 2000000
doc = nlp(combined_text)
# %%
# Create dictionaries to store the entities for each entity type
entity_dict = {
    'PERSON': {},
    'ORG': {},
    'PRODUCT': {},
    'EVENT': {},
    'MONEY': {},
    'DATE': {},
    'TIME': {},
    'LOC': {},
    'NORP': {}
}
# %%
# Iterating over the entities in the document and add them to the corresponding entity dictionary
for ent in doc.ents:
    if ent.label_ in entity_dict:
        if ent.text in entity_dict[ent.label_]:
            entity_dict[ent.label_][ent.text] += 1
        else:
            entity_dict[ent.label_][ent.text] = 1
# %%

# Removing stopwords and lemmatize the words
for key in entity_dict.keys():
    new_dict = {}
    for entity, count in entity_dict[key].items():
        entity = ' '.join([word.lemma_ for word in nlp(entity.lower()) if not word.is_stop])
        if entity in new_dict:
            new_dict[entity] += count
        else:
            new_dict[entity] = count
    entity_dict[key] = new_dict

# %% 
# Printing the top 5 entities for each entity type
for entity_type in entity_dict:
    print(entity_type)
    sorted_entities = sorted(entity_dict[entity_type], key=entity_dict[entity_type].get, reverse=True)[:5]
    for entity in sorted_entities:
        print(f"{entity}: {entity_dict[entity_type][entity]}")
    print()

# %%
