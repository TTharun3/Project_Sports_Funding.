#%%
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binned_statistic
os.getcwd()
#%%
# Loading the dataframe Main Data
#%%
cwd = os.getcwd()
cwd
#%%
cwd = cwd.replace("\\code", "")
cwd
#%%
main_data_df = pd.read_csv("{}\\data\\clean_data\\main_data_clean.csv".format(cwd))
main_data_df = main_data_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
main_data_df.head()
# %%
# Bar graph for Success Rate
count_df = pd.pivot_table(main_data_df, values = 'CampaignName', index='Success', aggfunc= 'count')
count_df = count_df.reset_index()
xlabels = count_df['Success'].to_list()
values = count_df['CampaignName'].to_list()
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(xlabels, values, color ='blue',
        width = 0.4)
plt.xlabel("Crowdfunding Outcome")
plt.ylabel("No. of campaigns")
plt.title("Distribution of success in sportscrowdfunding campaigns")
plt.show()

#%%
# Pie chart for Success Rate
values_pct = [i/1143*100 for i in values]
fig1, ax1 = plt.subplots()
ax1.pie(values_pct, labels = xlabels, autopct= '%1.1f%%')
ax1.axis('equal')
plt.xlabel("Crowdfunding Outcome")
plt.ylabel("%age of campaigns")
plt.title("Distribution of success in sportscrowdfunding campaigns")
plt.show()
plt.show()

# %%

# Plotting the histogram of AmountAdjusted
values, bins, bars =  plt.hist(main_data_df['AmountAdjusted'], bins=20, alpha=0.5, color = 'blue')
plt.xlabel("Funding Received (in USD) by Crowdfunding Campaigns")
plt.ylabel("Number of Campaigns")
plt.title = ('Funding Received Distrubtion')
plt.bar_label(bars, fontsize=10, color='navy')
plt.margins(x=0.01, y=0.1)
plt.xticks(bins, fontsize = 5)
plt.show()

#%%
# Plotting the histogram of Funds Raised Pct
values, bins, bars =  plt.hist(main_data_df['Funds Raised Pct'], bins=30, alpha=0.5, color = 'blue')
plt.xlabel("Funding Received (in USD) by Crowdfunding Campaigns")
plt.ylabel("Number of Campaigns")
plt.title = ('Funding Received Distrubtion')
plt.bar_label(bars, fontsize=10, color='navy')
plt.margins(x=0.01, y=0.1)
plt.xticks(bins, fontsize = 4)
plt.show()


#%%
# Bar graph for Country-wise distribution
count_df = pd.pivot_table(main_data_df, values = 'CampaignName', index='Country', aggfunc= 'count')
count_df = count_df.reset_index()
count_df = count_df.sort_values(by='CampaignName', ascending= False)
count_df_10 = count_df.iloc[0:10]
xlabels = count_df_10['Country'].to_list()
values = count_df_10['CampaignName'].to_list()
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.barh(xlabels, values, color ='blue',
        height = 0.4)
plt.xlabel("No. of crowdfunding campaigns")
plt.ylabel("Country")
plt.title("Country-wise distribution of crowdfunding campaigns")
plt.show()

# %%
# Bar graph for City-wise distribution
count_df = pd.pivot_table(main_data_df, values = 'CampaignName', index='City', aggfunc= 'count')
count_df = count_df.reset_index()
count_df = count_df.sort_values(by='CampaignName', ascending= False)
count_df_10 = count_df.iloc[0:10]
xlabels = count_df_10['City'].to_list()
values = count_df_10['CampaignName'].to_list()
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.barh(xlabels, values, color ='blue',
        height = 0.4)
plt.xlabel("No. of crowdfunding campaigns")
plt.ylabel("State")
plt.title("State-wise distribution of crowdfunding campaigns")
plt.show()

# %%
# Bar graph for Sport-wise distribution
count_df = pd.pivot_table(main_data_df, values = 'CampaignName', index='SportName', aggfunc= 'count')
count_df = count_df.reset_index()
count_df = count_df.sort_values(by='CampaignName', ascending= False)
count_df_10 = count_df.iloc[0:10]
xlabels = count_df_10['SportName'].to_list()
values = count_df_10['CampaignName'].to_list()
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.barh(xlabels, values, color ='blue',
        height = 0.4)
plt.xlabel("No. of crowdfunding campaigns")
plt.ylabel("Sport")
plt.title("Sport-wise distribution of crowdfunding campaigns")
plt.show()


# %%
# Box plots of % funds received for teams vs athletes 
main_data_df.boxplot(column='Funds Raised Pct', by='Team/Athlete')
plt.show()
#%%
xlabels
# %%
