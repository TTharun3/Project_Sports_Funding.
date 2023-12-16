#%%
from datetime import datetime
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os
import random
os.getcwd()

#%%
# Helper Functions

def get_true_text(tag):
    children = tag.find_elements(By.XPATH, '*')
    original_text = tag.text
    for child in children:
        original_text = original_text.replace(child.text, '', 1)
    return original_text


#%%
# Variable list
campaign_url_list = []
banner_list = []
total_donations_raised_list = []
percent_donation_list = []
total_required_donation_list = []
days_left_list = []
title_goal_list = []
parent_campaign_list = []
count_campaigns_list = []
count_supporters_list = []
name_campaigner_list = []
url_1_list = []
url_2_list = []
url_3_list = []
url_4_list = []
url_5_list = []
address_campaigner_list = []
type_of_sport_list = []
story_list = []
biography_list = []
contributer_name_list = []
contribution_amount_list = []
reward_amount_list = []
count_rewards_list = []
rewards_description_list = []
updates_comments_list = []

# Accessing clean data and creating dataframe 
#%%
cwd = os.getcwd()
cwd
#%%
cwd = cwd.replace("\\code", "")
cwd
#%%
campaign_df = pd.read_csv("{}\\data\\clean_data\\main_data_clean.csv".format(cwd))
campaign_df

#%%
driver_path = "C:\chromedriver\chromedriver.exe"
data_df = pd.DataFrame()

#%%
# Iterating over the rows in the dataframe
start_row = 1
for iter in range(start_row, campaign_df.shape[0]):

    campaign_url = campaign_df['CampaignUrlClean'].iloc[iter] #URL for specific campaigns
    driver = webdriver.Chrome(driver_path)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)

    driver.get(campaign_url)
    time.sleep(randint(10,15))
    
    # Campaign Main info
    try:
        raised_donation = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div[1]/div/div[2]").text
    except:
        raised_donation = "NULL"
    
    try:
        percent_value = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div[1]/div/div[3]").text
    except:
        percent_value = "NULL"

    try:
        requested_donation = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div[1]/div/div[4]").text
    except:
        requested_donation = "NULL"

    try:
        days_left = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div[2]/div/span[1]").text
    except:
        days_left = "NULL"

    try:
        title_goal = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[1]/div[1]/h1")
        title_goal_final = get_true_text(title_goal)
    except:
        title_goal_final = "NULL"
    
    try:
        parent_campaign = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[1]/div[1]/h1/span/a").text
    except:
        parent_campaign = "NULL"

    try:
        count_campaigns = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]").text
    except:
        count_campaigns = "NULL"

    try:
        count_supporters = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]").text
    except:
        count_supporters = "NULL"


    # Campaigner Info - name, social media links, website links
    try:
        campaigner_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]").text
    except:
        campaigner_name = "NULL"

    try:
        url_1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[1]").get_attribute('href')
    except:
        url_1 = "NULL"

    try:
        url_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[2]").get_attribute('href')
    except:
        url_2 = "NULL"

    try:
        url_3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[3]").get_attribute('href')
    except:
        url_3 = "NULL"
    
    try:
        url_5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[4]").get_attribute('href')
    except:
        url_5 = "NULL"

    try:
        url_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[4]").get_attribute('href')
    except:
        url_4 = "NULL"

    try:
        url_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/a[4]").get_attribute('href')
    except:
        url_4 = "NULL"


    # address of the campaigner
    try:
        type_of_sport = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[2]/div[1]/div[1]/div[1]/a").text
    except:
        type_of_sport = "NULL"

    try:
        story = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[1]/div[1]/div/div[1]/div[1]").text
    except:
        story = "NULL"

    try:
        biography = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[2]/div/div[1]/div[1]/div/div[2]/div").text
    except:
        biography = "NULL"

    campaign_url_list.append(campaign_url)
    total_donations_raised_list.append(raised_donation)
    percent_donation_list.append(percent_value)
    total_required_donation_list.append(requested_donation)
    days_left_list.append(days_left)
    title_goal_list.append(title_goal_final)
    parent_campaign_list.append(parent_campaign)
    count_campaigns_list.append(count_campaigns)
    count_supporters_list.append(count_supporters)
    name_campaigner_list.append(campaigner_name)
    url_1_list.append(url_1)
    url_2_list.append(url_2)
    url_3_list.append(url_3)
    url_4_list.append(url_4)
    url_5_list.append(url_5)
    # address_campaigner_list.append()
    type_of_sport_list.append(type_of_sport)
    story_list.append(story)
    biography_list.append(biography)

    if iter % 100 == 0:
        data = {'CampaignUrl': campaign_url_list, 'Donation Raised': total_donations_raised_list, '% Raised': percent_donation_list, 'Funding Goal': total_required_donation_list, 'Days Left': days_left_list,
        'Parent Campaign': parent_campaign_list, 'Creator Campaigns': count_campaigns_list, 'Creator Supporters': count_supporters_list, 'Sport Type': type_of_sport_list, 'Story': story_list,
        'Creator Bio': biography_list, 'Url 1': url_1_list, 'Url 2': url_2_list, 'Url 3': url_2_list, 'Url 4': url_4_list, 'Url 5': url_5_list}
        data_df = pd.DataFrame.from_dict(data)
        data_df.to_csv("c:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\Documents\\GitHub\\project-deliverable-1-invincible\\data\\raw_data\\campaigns\\campaign_raw_{}.csv".format(int(data_df.shape[0]) + 1))
    else:
        continue

    driver.quit()

# %%
data = {'CampaignUrl': campaign_url_list, 'Donation Raised': total_donations_raised_list, '% Raised': percent_donation_list, 'Funding Goal': total_required_donation_list, 'Days Left': days_left_list,
        'Parent Campaign': parent_campaign_list, 'Creator Campaigns': count_campaigns_list, 'Creator Supporters': count_supporters_list, 'Sport Type': type_of_sport_list, 'Story': story_list,
        'Creator Bio': biography_list, 'Url 1': url_1_list, 'Url 2': url_2_list, 'Url 3': url_2_list, 'Url 4': url_4_list, 'Url 5': url_5_list}
data_df = pd.DataFrame.from_dict(data)
data_df.to_csv("c:\\Users\\tharun\\OneDrive - Oklahoma A and M System\\Documents\\GitHub\\project-deliverable-1-invincible\\data\\raw_data\\campaigns\\campaign_raw_{}.csv".format(int(data_df.shape[0]) + 1))


