#%%
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os
os.getcwd()
#%%
cwd = os.getcwd()
cwd
#%%
cwd = cwd.replace("\\code", "")
cwd


#%%
# Data fields
campaign_name_list = []
campaign_url_list = [] # get attribute href appedn to https://sportfunder.com/ 
campaign_pic_url_list = [] # get attribute style
sport_list = []
sport_url_list = [] # get attribute href append to https://sportfunder.com/
short_desc_list = []
location_list = []
profile_pic_url_list = [] # get attribute style
raised_list = []
funded_list = []
daysleft_list = []
supporters_list = []
div_box_1_val_list = []
div_box_1_name_list = []
div_box_2_val_list = []
div_box_2_name_list = []
div_box_3_val_list = []
div_box_3_name_list = []
div_box_4_val_list = []
div_box_4_name_list = []

# xpaths for non-changing blocks
allcampaigns_xpath = "/html/body/div[1]/section/ul/li[7]/a"
loadmore_xpath = "/html/body/div[1]/section/div[1]/div[1]/div[2]/center/a"

#%%
driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.set_window_position(0,0)
driver.set_window_size(1920,1080)

sportfunder_url = "https://sportfunder.com/"
driver.get(sportfunder_url)

time.sleep(5)
# Opening the campaigns page
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/div/div/ul/li[2]/a").click()

time.sleep(5)

# Opening all campaigns page
driver.find_element(By.XPATH, "/html/body/div[1]/section/ul/li[7]/a").click()
time.sleep(5)

# Control Flags
# data_collected_flag = 0 # turns 1 if all data on the page is scraped
load_more_flag = 0 # turns 1 if all data collected flag turns 1

# Starting row
row_iter = int(input("Enter initial row number")) # check sys args to give the initial row number

# 

while row_iter < 100000:
    
    # check if iter div is present, if not load more
    try:
        print(row_iter)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[1]/div/div[1]/a/h5".format(row_iter))
        print("click worked")
        load_more_flag = 0
    except:
        load_more_flag = 1
    
    # each row has 3 campaigns
    # control flow for load more    
    if load_more_flag == 1 :
        driver.find_element(By.XPATH, loadmore_xpath).click()
        print("loaded more data")
        # row_iter += 1
        time.sleep(5)
    else: 
        for column_iter in range(1,4):
            sleep(1)
            try:
                campaign_name = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[1]/a/h5".format(row_iter, column_iter)).text
            except:
                campaign_name = "NULL"
            try:
                campaign_href = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[1]/a".format(row_iter, column_iter)).get_attribute('href')
                campaign_url = sportfunder_url + campaign_href
            except:
                campaign_url = "NULL"


            try:
                campaign_pic_href = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/a[1]/div".format(row_iter, column_iter)).get_attribute('style')
            except:
                campaign_pic_href = "NULL"
            try:
                profile_pic_href = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/a[2]/div".format(row_iter, column_iter)).get_attribute('style')
            except:
                profile_pic_href = "NULL"

            try:    
                sport_href = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[3]/a".format(row_iter, column_iter)).get_attribute('href')
                sport_url = sportfunder_url + sport_href
            except:
                sport_url = "NULL"
            try:
                sport = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[3]/a".format(row_iter, column_iter)).text
            except:
                sport = "NULL"
            try:
                short_desc = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/p".format(row_iter, column_iter)).text
            except:
                short_desc = "NULL"
            try:
                location = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[2]".format(row_iter, column_iter)).text
            except:
                location = "NULL"

            try:
                div_box_1_val = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[1]".format(row_iter, column_iter)).text
            except:
                div_box_1_val = "NULL"
            try:
                div_box_1_name = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[1]/small".format(row_iter, column_iter)).text
            except:
                div_box_1_name = "NULL"
            try:
                div_box_2_val = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[2]".format(row_iter, column_iter)).text
            except:
                div_box_2_val = "NULL"
            try:
                div_box_2_name = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[2]/small".format(row_iter, column_iter)).text
            except:
                div_box_2_name = "NULL"
            try:
                div_box_3_val = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[3]/span".format(row_iter, column_iter)).text
            except:
                div_box_3_val = "NULL"
            try:
                div_box_3_name = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[3]/small".format(row_iter, column_iter)).text
            except:
                div_box_3_name = "NULL"
            try:
                div_box_4_val = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[4]".format(row_iter, column_iter)).text
            except:
                div_box_4_val = "NULL"
            try:
                div_box_4_name = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[{}]/div[{}]/div/div[5]/div[4]/small".format(row_iter, column_iter)).text
            except:
                div_box_4_name = "NULL"

            campaign_name_list.append(campaign_name)
            campaign_url_list.append(campaign_url) 
            campaign_pic_url_list.append(campaign_pic_href)
            sport_list.append(sport)
            sport_url_list.append(sport_url) 
            short_desc_list.append(short_desc)
            location_list.append(location)
            profile_pic_url_list.append(profile_pic_href)
            div_box_1_val_list.append(div_box_1_val)
            div_box_1_name_list.append(div_box_1_name)
            div_box_2_val_list.append(div_box_2_val)
            div_box_2_name_list.append(div_box_2_name)
            div_box_3_val_list.append(div_box_3_val)
            div_box_3_name_list.append(div_box_3_name)
            div_box_4_val_list.append(div_box_4_val)
            div_box_4_name_list.append(div_box_4_name)
             
            # print(row_iter, column_iter)
            # print(campaign_name, sport, short_desc, location) 
            # print(div_box_1_val, div_box_1_name)
            # print(div_box_2_val, div_box_2_name)
            # print(div_box_3_val, div_box_3_name)
            # print(div_box_4_val, div_box_4_name)
            # print(campaign_href, sport_href)
            # print(campaign_pic_href)
            # print(profile_pic_href)
            
        row_iter += 1
    
    if row_iter % 100 == 0:
        print(row_iter)
        data = {'CampaignName': campaign_name_list, 'CampaignUrl': campaign_url_list, 'CampaignPicUrl': campaign_pic_url_list, 'ProfilePicUrl': profile_pic_url_list, 
                'SportName': sport_list, 'SportUrl': sport_url_list, 'ShortDescription': short_desc_list, 'Location': location_list, 
                'DivBox1Val': div_box_1_val_list, 'DivBox1Name': div_box_1_name_list, 'DivBox2Val': div_box_2_val_list, 'DivBox2Name': div_box_2_name_list,
                'DivBox3Val': div_box_3_val_list, 'DivBox3Name': div_box_3_name_list, 'DivBox4Val': div_box_4_val_list, 'DivBox4Name': div_box_4_name_list}
        df = pd.DataFrame.from_dict(data)

#%%
        df.to_csv("{}\\data\\raw_data\\raw_main_{}.csv".format(cwd,row_iter))


driver.quit()


#%%
data = {'CampaignName': campaign_name_list, 'CampaignUrl': campaign_url_list, 'CampaignPicUrl': campaign_pic_url_list, 'ProfilePicUrl': profile_pic_url_list, 
                'SportName': sport_list, 'SportUrl': sport_url_list, 'ShortDescription': short_desc_list, 'Location': location_list, 
                'DivBox1Val': div_box_1_val_list, 'DivBox1Name': div_box_1_name_list, 'DivBox2Val': div_box_2_val_list, 'DivBox2Name': div_box_2_name_list,
                'DivBox3Val': div_box_3_val_list, 'DivBox3Name': div_box_3_name_list, 'DivBox4Val': div_box_4_val_list, 'DivBox4Name': div_box_4_name_list}
df = pd.DataFrame.from_dict(data)
df.to_csv("{}\\data\\raw_data\\raw_data_main.csv".format(cwd))

#%%

# Loading more pages
for iter in range(1, 10):
    driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/center/a").click()
    time.sleep(5)

# Going to one campaign
driver.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/a").click()
time.sleep(5)

# Going back to all campaigns
driver.back()
time.sleep(10)
driver.quit()
# %%
