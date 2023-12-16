#%%
import os
import numpy as np
import pandas as pd

# Project Directory
cwd = os.getcwd()
cwd = cwd.replace("/code", "")

# Accessing CSVs and creating DataFrame
#%%
cwd = os.getcwd()
cwd
#%%
cwd = cwd.replace("\\code", "")
cwd

#%%
df1 = pd.read_csv("{}\\data\\clean_data\\main_data_clean.csv".format(cwd))
df1
#%%
df2 = pd.read_csv("{}\\data\\raw_data\\raw_data_campaignstories.csv".format(cwd))
df2

#%%
# Joining 2 dataframes using Left join
df = df1.merge(df2, left_on='CampaignUrlClean' , right_on='CampaignUrl', how='left')

#%%
# Dropping Unnamed columns
df = df.drop(columns = 'Unnamed: 0.1', axis = 1)
df = df.drop(columns = 'Unnamed: 0_x', axis = 1)
df = df.drop(columns = 'Unnamed: 0_y', axis = 1)

#%%
df.to_csv("Temp.csv")
#%%
df.head()

#%%
df.columns

#%%
# Dropping unnecessary columns
df = df.drop(columns=['Campaign URL cleaned','Profile URL cleaned',
                 'CampaignUrl','%Raised','Funding Goal',
                 'Days Left','Url 1', 'Url 2', 'Url 3', 'Url 4', 'Url 5'])

#%%
# creating final dataframe with Renamed columns
df = df.rename(columns = {"Money Raised":"FundsRaised",
                     "CampaignUrlClean":"CampaignURL",
                     "number of supporters":"numSupporters",
                     "Funds Raised Pct":"FundsRaisedPercent",
                     "Team/Athlete":"TeamOrAthlete",
                     "Donation Raised":"DonationRaised",
                     "Parent Campaign":"ParentCampaign",
                     "Creator Campaigns":"CreatorCampaigns",
                     "Creator Supporters":"CreatorSupporters",
                     "Sport Type":"SportType",
                     "Creator Bio":"CreatorBio"})




# %%
df.to_csv("C:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\MAIN DRIVE\\Semester 2\\MSIS5223 (Programming for Data Science and Analytics 2)\\project-deliverable-1-bazinga\\data\\clean_data\\Final_Data_Merged.csv", index = False)
# %%
df.columns

# %%
# Project Directory
cwd = os.getcwd()
cwd = cwd.replace("/code", "")

main_df = pd.read_csv("{}/data/clean_data/final_data_merged_storycleaned.csv".format(cwd))
main_df = main_df.set_index('CampaignURL')
print(main_df.shape)
#%%
# print(main_df.head())
# Creating dimensional word counts for each narcissism dimension
for dimension in ['authority', 'superiority', 'exhibitionism', 'vanity', 'selfsufficiency', 'entitlement', 'exploitativeness']:
    df = pd.read_csv("{}/data/narcissism_raw_data/{}_rawscores.csv".format(cwd, dimension))
    df = df.set_index(['CampaignURL'])
    main_df[dimension] = df.sum(axis = 1)
    # print(df.shape)
    # print(df[dimension].head())
    # main_df = main_df.merge(df[dimension], how='left', on='CampaignURL')
    print(main_df.shape)

main_df.head()
main_df.to_csv("{}/data/clean_data/final_data_merged_storycleaned_wordcounts.csv".format(cwd))
# %%
main_df.columns
# %%
# Creation of Final Dataset
# Factor Analysis output
# authority - 0.612, superiority - 0.9, exhibitionism - 0.92, vanity - 0.737, selfsufficiency - 0.628
# entitlement - 0.509
main_df['NarcissismFactor'] = main_df['authority'] * 0.612 + main_df['superiority'] * 0.9 \
                            + main_df['exhibitionism'] * 0.92 + main_df['vanity'] * 0.737 \
                            + main_df['selfsufficiency'] * 0.628 + main_df['entitlement'] * 0.509


main_df = main_df.drop(columns = ['authority', 'superiority', 'exhibitionism', 'vanity', 'selfsufficiency', 'entitlement', 'exploitativeness'])
main_df.to_csv("{}/data/clean_data/final_dataset_analysis.csv".format(cwd))

# %%
main_df.columns

# sentiment Analysis - Joy and Sadness, Positive and Negative, and Fear and Trust Grouping to main csv file

#%%
import pandas as pd
import os
#%%
# read the joy_sadness_raw_data csv file
df = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/joy_sadness_raw_data.csv')
#%%
sentiment_df = df.pivot_table(index=['CampaignURL'], columns=['sentiment'], aggfunc='size', fill_value=0)
#%%
main_df = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis.csv")
main_df.head()
#%%
main_df = main_df.merge(sentiment_df, on='CampaignURL', how='left')
main_df
#%%
main_df.to_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score.csv", index=False)

#%%
import pandas as pd
#%%
# read the pos_neg_raw_data.csv file
df = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/pos_neg_raw_data.csv')
#%%
sentiment_df = df.pivot_table(index=['CampaignURL'], columns=['sentiment2'], aggfunc='size', fill_value=0)
#%%
#main_df = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis.csv")
#main_df.head()
#%%
main_df = main_df.merge(sentiment_df, on='CampaignURL', how='left')
main_df
#%%
main_df.to_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score.csv", index=False)

# %%
#%%
import pandas as pd
#%%
# read the CSV file trust_fear_raw_data.csv
df = pd.read_csv('E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/trust_fear_raw_data.csv')
#%%
sentiment_df = df.pivot_table(index=['CampaignURL'], columns=['sentiment3'], aggfunc='size', fill_value=0)
#%%
#main_df = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis.csv")
#main_df.head()
#%%
main_df = main_df.merge(sentiment_df, on='CampaignURL', how='left')
main_df
#%%
main_df.to_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis_sentiment_score.csv", index=False)

# %%
