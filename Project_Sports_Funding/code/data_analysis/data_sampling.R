# Installing packages if necessary
# install.packages('dplyr')
# install.packages('languageserver')
# install.packages('httpgd')
install.packages('Hmisc')

# Use if in VSCode
# library(languageserver)
# library(httpgd)

library(dplyr)
library(Hmisc)

# Loading the sentiment scores updated dataset
df <- read.csv(paste(getwd(),"/data/clean_data/final_dataset_textanalysis_sentiment_score.csv",sep=""),header = T)
analysis_df = df %>% 
  select(CampaignURL, numSupporters, TeamOrAthlete, AmountAdjusted, Success, Wordcount, NarcissismFactor, 
         joy, sadness, negative, positive, fear, trust, FundingGoalAdjusted)

write.csv(analysis_df, paste(getwd(),"/data/data_analysis/raw_dataset_withsentimentscores.csv",sep=""))

analysis_df2 <- read.csv(paste(getwd(),"/data/data_analysis/raw_dataset_withsentimentscores_withouterrors.csv",sep=""),header = T)

# dropping duplicates based on CampaignURL
analysis_df2 <- analysis_df2[!duplicated(analysis_df2$CampaignURL), ]
# only considering the complete cases
analysis_df2 <- analysis_df2[complete.cases(analysis_df2),]

# Modifying the types of categorical variables
analysis_df2$Success <- as.factor(ifelse(analysis_df2$Success == "success", "success", "fail"))
analysis_df2$TeamOrAthlete <- as.factor(analysis_df2$TeamOrAthlete)
# Converting certain variables into numeric types 
analysis_df2$AmountAdjusted <- as.numeric(analysis_df2$AmountAdjusted)
analysis_df2$FundingGoalAdjusted <- as.numeric(analysis_df2$FundingGoalAdjusted)

plot(analysis_df2$Success)

# Train-Test split of 80-20 
# Since low sample size, higher train amount will benefit training
# Cross-validation can be used
# Stratified sampling to maintain distributions of Success, TeamorAthlete

# Creating an ID vector
analysis_df2$id <- 1:nrow(analysis_df2)

analysis_df2_train <- analysis_df2 %>%
  group_by(Success, TeamOrAthlete) %>%
  mutate(num_rows=n()) %>%
  sample_frac(0.8, weight=num_rows) %>%
  ungroup

analysis_df2_test <- anti_join(analysis_df2, analysis_df2_train, by='id')

write.csv()



# Checking distribution of Success variable in train and test data
par(mfrow = c(1,2))
plot(analysis_df2_train$Success)
title("Counts of successful and failed campaigns in Train Data")
plot(analysis_df2_test$Success)
title("Counts of successful and failed campaigns in Test Data")

# Checking distribution of TeamorAthlete variable in train and test data
par(mfrow = c(1,2))
plot(analysis_df2_train$TeamOrAthlete)
title("Counts of Team and Athlete campaigns in Train Data")
plot(analysis_df2_test$TeamOrAthlete)
title("Counts of Team and Athlete campaigns in Test Data")


di <- describe(analysis_df2_test)

sd(analysis_df2_test$numSupporters)


write.csv(analysis_df2_train, paste(getwd(),"/data/data_analysis/final_data_train.csv",sep=""))
write.csv(analysis_df2_test, paste(getwd(),"/data/data_analysis/final_data_test.csv",sep=""))


# T-tests to test differences in means of numerical variables
t.test(analysis_df2_train$numSupporters, analysis_df2_test$numSupporters)
t.test(analysis_df2_train$AmountAdjusted, analysis_df2_test$AmountAdjusted)
t.test(analysis_df2_train$Wordcount, analysis_df2_test$Wordcount)
t.test(analysis_df2_train$NarcissismFactor, analysis_df2_test$NarcissismFactor)
t.test(analysis_df2_train$joy, analysis_df2_test$joy)
t.test(analysis_df2_train$sadness, analysis_df2_test$sadness)
t.test(analysis_df2_train$positive, analysis_df2_test$positive)
t.test(analysis_df2_train$negative, analysis_df2_test$negative)
t.test(analysis_df2_train$fear, analysis_df2_test$fear)
t.test(analysis_df2_train$trust, analysis_df2_test$trust)
t.test(analysis_df2_train$FundingGoalAdjusted, analysis_df2_test$FundingGoalAdjusted)

