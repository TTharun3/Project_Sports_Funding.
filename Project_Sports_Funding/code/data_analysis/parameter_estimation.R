# install packages if necessary
# install.packages('Hmisc')
# install.packages('pROC')
# install.packages('gridExtra')
# install.packages('ggpubr')
# install.packages('DAAG')
# install.packages('tree')
# install.packages('caret')
# install.packages('mlbench')
# install.packages('rpart.plot')
# install.packages('party')

# Loading libraries
library(Hmisc)
library(pROC)
library(ggplot2)
library(gridExtra)
library(ggpubr)
library(car)
library(DAAG)
library(party)
library(rpart)
library(rpart.plot)
library(mlbench)
library(caret)
library(tree)
library(dplyr)



# Loading the train and test datasets
train_df <- read.csv(paste(getwd(),"/data/data_analysis/final_data_train.csv",sep=""))
test_df <- read.csv(paste(getwd(),"/data/data_analysis/final_data_test.csv",sep=""))

# Transforming numerical variables to adjust for skewness
# numSupporters, Wordcount, NarcissismFactor, joy, sadness, negative, positive
# fear, trust, FundingGoalAdjusted
# adding 1 so that zero values are not affected 
train_df$lognumSupporters <- log10(train_df$numSupporters + 1)
train_df$logWordcount <- log10(train_df$Wordcount + 1)
train_df$logNarcissismFactor <- log10(train_df$NarcissismFactor + 1)
train_df$logJoy <- log(train_df$joy + 1)
train_df$logSadness <- log(train_df$sadness + 1)
train_df$logNegative <- log(train_df$negative + 1)
train_df$logPositive <- log(train_df$positive + 1)
train_df$logFear <- log(train_df$fear + 1)
train_df$logTrust <- log(train_df$trust + 1)
train_df$logFundingGoalAdjusted <- log10(train_df$FundingGoalAdjusted + 1)

test_df$lognumSupporters <- log10(test_df$numSupporters + 1)
test_df$logWordcount <- log10(test_df$Wordcount + 1)
test_df$logNarcissismFactor <- log10(test_df$NarcissismFactor + 1)
test_df$logJoy <- log(test_df$joy + 1)
test_df$logSadness <- log(test_df$sadness + 1)
test_df$logNegative <- log(test_df$negative + 1)
test_df$logPositive <- log(test_df$positive + 1)
test_df$logFear <- log(test_df$fear + 1)
test_df$logTrust <- log(test_df$trust + 1)
test_df$logFundingGoalAdjusted <- log10(test_df$FundingGoalAdjusted + 1)

# Evaluating the distributions of transformed variables
# Checking distribution of Success variable in train and test data
# numSupporters
hist1 <- ggplot(train_df, aes(x=numSupporters), ) + geom_histogram() + ggtitle("Distribution of numSupporters")
hist2 <- ggplot(train_df, aes(x=lognumSupporters)) + geom_histogram() + ggtitle("Distribution of lognumSupporters")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$numSupporters, pch = 1, frame = FALSE)
qqline(train_df$numSupporters, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$lognumSupporters, pch = 1, frame = FALSE)
qqline(train_df$lognumSupporters, col = "steelblue", lwd = 2)


# wordcount
hist1 <- ggplot(train_df, aes(x=Wordcount), ) + geom_histogram() + ggtitle("Distribution of Wordcount")
hist2 <- ggplot(train_df, aes(x=logWordcount)) + geom_histogram() + ggtitle("Distribution of logWordcount")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$Wordcount, pch = 1, frame = FALSE)
qqline(train_df$Wordcount, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logWordcount, pch = 1, frame = FALSE)
qqline(train_df$logWordcount, col = "steelblue", lwd = 2)

# joy
hist1 <- ggplot(train_df, aes(x=joy), ) + geom_histogram() + ggtitle("Distribution of joy")
hist2 <- ggplot(train_df, aes(x=logJoy)) + geom_histogram() + ggtitle("Distribution of logJoy")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$joy, pch = 1, frame = FALSE)
qqline(train_df$joy, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logJoy, pch = 1, frame = FALSE)
qqline(train_df$logJoy, col = "steelblue", lwd = 2)

# sadness
hist1 <- ggplot(train_df, aes(x=sadness), ) + geom_histogram() + ggtitle("Distribution of Sadness")
hist2 <- ggplot(train_df, aes(x=logSadness)) + geom_histogram() + ggtitle("Distribution of logSadness")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$sadness, pch = 1, frame = FALSE)
qqline(train_df$sadness, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logSadness, pch = 1, frame = FALSE)
qqline(train_df$logSadness, col = "steelblue", lwd = 2)

# positive
hist1 <- ggplot(train_df, aes(x=positive), ) + geom_histogram() + ggtitle("Distribution of positive sentiment")
hist2 <- ggplot(train_df, aes(x=logPositive)) + geom_histogram() + ggtitle("Distribution of log of positive sentiment")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$positive, pch = 1, frame = FALSE)
qqline(train_df$positive, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logPositive, pch = 1, frame = FALSE)
qqline(train_df$logPositive, col = "steelblue", lwd = 2)

# negative
hist1 <- ggplot(train_df, aes(x=negative), ) + geom_histogram() + ggtitle("Distribution of negative sentiment")
hist2 <- ggplot(train_df, aes(x=logNegative)) + geom_histogram() + ggtitle("Distribution of log of negative sentiment")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$negative, pch = 1, frame = FALSE)
qqline(train_df$negative, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logNegative, pch = 1, frame = FALSE)
qqline(train_df$logNegative, col = "steelblue", lwd = 2)

# fear
hist1 <- ggplot(train_df, aes(x=fear), ) + geom_histogram() + ggtitle("Distribution of fear sentiment")
hist2 <- ggplot(train_df, aes(x=logFear)) + geom_histogram() + ggtitle("Distribution of log of fear sentiment")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$fear, pch = 1, frame = FALSE)
qqline(train_df$fear, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logFear, pch = 1, frame = FALSE)
qqline(train_df$logFear, col = "steelblue", lwd = 2)

# trust
hist1 <- ggplot(train_df, aes(x=trust), ) + geom_histogram() + ggtitle("Distribution of trust sentiment")
hist2 <- ggplot(train_df, aes(x=logTrust)) + geom_histogram() + ggtitle("Distribution of log of trust sentiment")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$trust, pch = 1, frame = FALSE)
qqline(train_df$trust, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logTrust, pch = 1, frame = FALSE)
qqline(train_df$logTrust, col = "steelblue", lwd = 2)

# Funding Goal
hist1 <- ggplot(train_df, aes(x=FundingGoalAdjusted), ) + geom_histogram() + ggtitle("Distribution of Funding Goal")
hist2 <- ggplot(train_df, aes(x=logFundingGoalAdjusted)) + geom_histogram() + ggtitle("Distribution of log of Funding Goal")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$FundingGoalAdjusted, pch = 1, frame = FALSE)
qqline(train_df$FundingGoalAdjusted, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logFundingGoalAdjusted, pch = 1, frame = FALSE)
qqline(train_df$logFundingGoalAdjusted, col = "steelblue", lwd = 2)

# Narcissism Factor
hist1 <- ggplot(train_df, aes(x=NarcissismFactor), ) + geom_histogram() + ggtitle("Distribution of Narcissism Factor")
hist2 <- ggplot(train_df, aes(x=logNarcissismFactor)) + geom_histogram() + ggtitle("Distribution of log of Narcissism Factor")
ggarrange(hist1, hist2, ncol = 2, nrow = 1)
qqnorm(train_df$NarcissismFactor, pch = 1, frame = FALSE)
qqline(train_df$NarcissismFactor, col = "steelblue", lwd = 2)
qqnorm2 <- qqnorm(train_df$logNarcissismFactor, pch = 1, frame = FALSE)
qqline(train_df$logNarcissismFactor, col = "steelblue", lwd = 2)


# Converting categorical variables into factor variables
train_df$Success <- as.factor(train_df$Success)
train_df$TeamOrAthlete <- as.factor(train_df$TeamOrAthlete)
test_df$Success <- as.factor(test_df$Success)
test_df$TeamOrAthlete <- as.factor(test_df$TeamOrAthlete)



# Building logistic regression to predict Success
logreg1 <- glm(Success ~ TeamOrAthlete + logFundingGoalAdjusted
                        # + lognumSupporters
                        # + logWordcount
                        + logNarcissismFactor 
                        + logTrust + logFear
                        # + logPositive
                        + logNegative
                        + logJoy + logSadness, 
                        family = "binomial",
                        data = train_df)

summary(logreg1)
vif(logreg1)

Anova(logreg1)

# Calculating AUC of logistic regression model
predicted <- predict(logreg1, test_df, type = "response")
auc(test_df$Success, predicted)


# Decision Tree
set.seed(1234)
train_decisiontree <- train_df %>% 
  select(TeamOrAthlete, logFundingGoalAdjusted, logNarcissismFactor, logTrust, logFear,
         logNegative, logJoy, logSadness)
test_decisiontree <- test_df %>% 
  select(TeamOrAthlete, logFundingGoalAdjusted, logNarcissismFactor, logTrust, logFear,
         logNegative, logJoy, logSadness)

# Building an unpruned decision tree with Gini index as the primary metric
dectree1 <- tree(Success~., train_decisiontree, mindev=1e-6, minsize=2, split = 'gini' ) 
plot(dectree1)
text(dectree1)

# Finding the best tradeoff for deviance and cost-complexity
pruneddectree1 <- prune.tree(dectree1)
plot(pruneddectree1)

# Best decision tree considering deviance and cost-complexity is at 12 terminal nodes
pruneddectree2 <- prune.tree(dectree1, best = 12)
pruneddectree2
plot(pruneddectree2)
text(pruneddectree2)

# Calculating AUC for unpruned decision tree
predicted <- predict(dectree1, test_decisiontree, type = "vector")
auc(test_df$Success, predicted[,2])

# Calculating AUC for pruned decision tree
predicted <- predict(pruneddectree2, test_decisiontree, type = "vector")
auc(test_df$Success, predicted[,2])