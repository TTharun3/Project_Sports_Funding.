#%%
import pandas as pd
import numpy as np
import os
import re

#%%
# Functions for cleaning data

# removing redundant text from campaign urls
def clean_campaignurl(row):
	campaignurl_unclean = str(row['CampaignUrl'])
	campaignurl_clean = campaignurl_unclean.removeprefix('https://sportfunder.com/')
	return campaignurl_clean

# dividing the teams and athelets 
def clean_sporturl_team(row):
    sporturl_unclean = str(row['SportUrl'])
    sporturl_clean = sporturl_unclean.removeprefix('https://sportfunder.com/https://sportfunder.com/')
    sporturl_clean_final = sporturl_clean.split("/", 1)[0]
    return sporturl_clean_final

# Removing \r\nRaised from DivBox1Val
def clean_money_raised(row):
    moneyraised_unclean = str(row['DivBox1Val'])
    moneyraised_clean = moneyraised_unclean.removesuffix("\r\nRaised")
    return moneyraised_clean

# Removing Funded from DivBox2Val
def per_funded(row):
    funded_unclean = str(row['DivBox2Val'])
    funded_clean = funded_unclean.removesuffix("%\r\nFunded")
    return funded_clean

# Removing Supporters from DivBox4Val
def nof_supporters(row):
    supporter_unclean = str(row['DivBox4Val'])
    supporter_clean = supporter_unclean.removesuffix("\r\nSupporters")
    return supporter_clean

# Removing text from Campaign Pic Url
def clean_campaignpicurl(row):
    cppicurl_unclean = str(row['CampaignPicUrl'])
    cppicurl_clean = cppicurl_unclean.removeprefix('background-image: url("')
    cppicurl_clean_1 = cppicurl_clean.removesuffix("\");")
    
    return cppicurl_clean_1
 
# Removing the extra Sport URl 
def clean_sporturl(row):
    sporturl_unclean = str(row['SportUrl'])
    sporturl_clean = sporturl_unclean.removeprefix('https://sportfunder.com/')
    return sporturl_clean

# Success variable - 1 if successful, 0 if failed
def crowdfunding_outcome(row):
    fundsraisedpct = int(row['Funds Raised Pct'])
    if fundsraisedpct > 100 :
        return 1
    else:
        return 0



df_raw = pd.DataFrame()
for file in os.listdir("C:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\MAIN DRIVE\\MSIS5193 (Programming for Data Science)\\project-deliverable-1-invincible\\data\\raw_data"):
    df_file = pd.read_csv("C:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\MAIN DRIVE\\MSIS5193 (Programming for Data Science)\\project-deliverable-1-invincible\\data\\raw_data\\{}".format(file))
    df_raw = pd.concat([df_file, df_raw], ignore_index = True)
    df_raw = df_raw.append(df_file, ignore_index = True)
    del(df_file)

df_raw.shape
df_raw




#%%
# Removing Duplicates from Raw Data
df_raw = df_raw.drop_duplicates(ignore_index= True, keep= 'last')
df_raw.shape


# %%
# Data Cleaning

## 1. Copying raw data to clean data 
df_clean = df_raw
df_clean
# %%
## 2. Cleaning the campaign URLs 
df_clean['CampaignUrlClean'] = df_clean.apply(clean_campaignurl, axis= 1)
df_clean

## 3. Cleaning money raised
df_clean['Money Raised'] = df_clean.apply(clean_money_raised, axis= 1)
df_clean

## 4. Campaign Pic URL
df_clean['Campaign URL cleaned'] = df_clean.apply(clean_campaignpicurl, axis= 1)
df_clean

## 5. Profile Pic URL
df_clean['Profile URL cleaned'] = df_clean.apply(clean_campaignpicurl, axis= 1)
df_clean

## 6. Cleaning the Sport URLs 
df_clean['SportUrlClean'] = df_clean.apply(clean_sporturl, axis= 1)
df_clean

## 7. Cleaning Fund raised
df_clean['number of supporters'] = df_clean.apply(nof_supporters, axis= 1)
df_clean

## 8. Cleaning number of supporters
df_clean['Funds Raised Pct'] = df_clean.apply(per_funded, axis= 1)
df_clean



#%%
# Data Transformation
## 1. Location string split
df_clean[['City', 'State', 'Country']] = df_clean['Location'].str.split(pat= ", ", expand= True)
df_clean

#%%
## 2. Identifying Currency
df_clean['Currency'] = df_clean['Money Raised'].str[0]
df_clean['Amount'] = df_clean['Money Raised'].str[1:]
df_clean['Currency'] = np.where(df_clean['Currency'] == '$', 'USD', df_clean['Currency'])
df_clean['Currency'] = np.where(df_clean['Currency'] == '¥', 'Japanese Yen', df_clean['Currency'])
df_clean['Currency'] = np.where(df_clean['Currency'] == '£', 'Pound', df_clean['Currency'])
df_clean['Currency'] = np.where(df_clean['Currency'] == '₽', 'Russian Rubel', df_clean['Currency'])
df_clean['Currency'] = np.where(df_clean['Currency'] == '€', 'Euro', df_clean['Currency'])
df_clean
#%%

## 3. Extracting single athlete / teams from Sport URL 
df_clean['Team/Athlete'] = df_clean.apply(clean_sporturl_team, axis= 1)
df_clean

#%%
## 4. Creating the Success variable based on Funds Raised Pct
df_clean['Success'] = df_clean.apply(crowdfunding_outcome, axis = 1)
df_clean

#%%
## 5. Dropping the coloumns which have been transformed

df_clean.drop(['CampaignUrl', 'CampaignPicUrl', 'ProfilePicUrl', 'SportUrl','Location','DivBox1Val','DivBox1Name','DivBox2Val','DivBox2Name','DivBox3Val','DivBox3Name','DivBox4Val','DivBox4Name',], axis=1, inplace=True)
df_clean






df_clean.to_csv("C:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\MAIN DRIVE\\MSIS5193 (Programming for Data Science)\\project-deliverable-1-invincible\\data\\clean_data\\main_data_clean.csv")

# %%

#imports for missing Data
import seaborn as sns
import pandas as pd
import missingno as msno

# creating datafrmame from fina; merged data
#%%
cwd = os.getcwd()
cwd
#%%
cwd = cwd.replace("\\code", "")
cwd
#%%
main_data_df = pd.read_csv("{}\\data\\clean_data\\Final_Data_Merged.csv".format(cwd))
main_data_df.info()
# %%
# plotting missing values
msno.bar(main_data_df)
# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import statsmodels.api as sm

outlier_det_df = pd.read_csv("{}\\data\\clean_data\\final_dataset_analysis.csv".format(cwd))
outlier_det_df.info()
plot_df = outlier_det_df.loc[:, ['numSupporters', 'FundsRaisedPercent','Success','AmountAdjusted','Wordcount','NarcissismFactor']]
plot_df
# %%

# QQ plots
fig, ax = plt.subplots(2, 3, figsize=(16, 12))

for i, col in enumerate(plot_df.columns):
    sm.qqplot(plot_df[col], line='s', ax=ax[i//3, i%3])
    ax[i//3, i%3].set_title(f'QQ plot for {col}')

plt.show()
# %%
# histograms
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,8))

for i, col in enumerate(plot_df.columns):
    plot_df[col].plot.hist(ax=axes[i//3, i%3], bins=10)
    axes[i//3, i%3].set_title(f'Histogram of {col}')
    axes[i//3, i%3].set_xlabel(col)

fig.tight_layout()
plt.show()
# %%

# Apply log transformation to the dataframe
log_df = np.log(plot_df.abs() + 1)

# Create box plots for each variable
fig, ax = plt.subplots(2, 3, figsize=(12, 8))

for i, col in enumerate(log_df.columns):
    ax[i//3, i%3].boxplot(log_df[col])
    ax[i//3, i%3].set_title(f'Box plot for {col}')

plt.show()
# %%
