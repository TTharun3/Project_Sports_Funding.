# Loading packages
library(tidyverse)
library(tidytext)
library(SnowballC)
library(wordcloud)
library(udpipe)
library(lattice)

# Loading the raw text data from data > clean_data folder
raw_data <- read.csv(paste(getwd(),"/data/clean_data/final_dataset_textanalysis.csv",sep = ""))

# Selecting only english story texts and campaigns with stories
raw_data <- raw_data[raw_data['language'] == "en",]

# Selecting the story texts
story_texts_data = select(raw_data, Story_Original, CampaignURL)

tidy_storytext = unnest_tokens(story_texts_data, word, Story_Original)

# Stop word removal

data("stop_words")
tidy_storytext2 = tidy_storytext %>% 
  anti_join(stop_words)

patterndigits = '\\b[0-9]+\\b'

tidy_storytext2$word = tidy_storytext2$word %>%
  str_remove_all(patterndigits)

tidy_storytext2$word = tidy_storytext2$word %>%
  str_replace_all('[:space:]', '')

tidy_storytext3 = tidy_storytext2 %>% 
  filter(!(word == ''))

tidy_storytext4 = tidy_storytext3 %>%
  mutate_at("word", funs(wordStem((.), language="en")))

<<<<<<< HEAD

# Sentiment Analysis 
# Evaluating joy and sadness
nrc_joysad = get_sentiments('nrc') %>%
  filter(sentiment == 'joy' | 
           sentiment == 'sadness')

newjoin = inner_join(tidy_storytext4, nrc_joysad)

write.csv(newjoin, paste(getwd(),"/data/text_analysis_data/joy_sadness_raw_data.csv",sep = ""))

# Evaluating trust and fear
nrc_trstfear = get_sentiments('nrc') %>%
  filter(sentiment == 'trust' |
           sentiment == 'fear')

newjoin2 = inner_join(tidy_storytext4, nrc_trstfear)
write.csv(newjoin2, paste(getwd(),"/data/text_analysis_data/trust_fear_raw_data.csv",sep = ""))

# Evaluating positive and negative
nrc_posneg = get_sentiments('nrc') %>%
  filter(sentiment == 'positive' |
           sentiment == 'negative')

newjoin3 = inner_join(tidy_storytext4, nrc_posneg)
write.csv(newjoin3, paste(getwd(),"/data/text_analysis_data/pos_neg_raw_data.csv",sep = ""))

# 
counts = count(newjoin, word, sentiment)
spread2 = spread(counts, sentiment, n, fill = 0)
spread2

content_data = mutate(spread2, contentment = joy - sadness, linenumber = row_number())
storytext_joysad = arrange(content_data, desc(contentment))
storytext_joysad
=======
# Top 10 words for all sentiments and word clouds

### Joy
JoySadData <- read.csv(paste(getwd(),"/data/text_analysis_data/joy_sadness_raw_data.csv",sep = ""))
Joy =  JoySadData %>% 
  filter(sentiment == "joy")
countJoy = count(Joy, word, sort = TRUE)
countJoy = rename(countJoy, freq = n)
Joy2 = top_n(countJoy, 10)

#Word cloud for joy
wordcloud(Joy[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

### Sadness
Sadness =  JoySadData %>% 
  filter(sentiment == "sadness")
countSadness = count(Sadness, word, sort = TRUE)
countSadness = rename(countSadness, freq = n)
Sadness2 = top_n(countSadness, 10)

#Word cloud for joy
wordcloud(Sadness[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

### Positive
PosNegData <- read.csv(paste(getwd(),"/data/text_analysis_data/pos_neg_raw_data.csv",sep = ""))
Positive =  PosNegData %>% 
  filter(sentiment == "positive")
countPositive = count(Positive, word, sort = TRUE)
countPositive = rename(countPositive, freq = n)
Positive2 = top_n(countPositive, 10)

#Word cloud for Positive
wordcloud(Positive[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

### Negative
Negative =  PosNegData %>% 
  filter(sentiment == "negative")
countNegative = count(Negative, word, sort = TRUE)
countNegative = rename(countNegative, freq = n)
Negative2 = top_n(countNegative, 10)

#Word cloud for Negative
wordcloud(Negative[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

### Trust
TrustFearData <- read.csv(paste(getwd(),"/data/text_analysis_data/trust_fear_raw_data.csv",sep = ""))
Trust =  TrustFearData %>% 
  filter(sentiment == "trust")
countTrust= count(Trust, word, sort = TRUE)
countTrust = rename(countTrust, freq = n)
Trust2 = top_n(countTrust, 10)

#Word cloud for Positive
wordcloud(Trust[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

### Fear
Fear =  TrustFearData %>% 
  filter(sentiment == "fear")
countFear= count(Fear, word, sort = TRUE)
countFear = rename(countFear, freq = n)
Fear2 = top_n(countFear, 10)

#Word cloud for Positive
wordcloud(Fear[,3],
          max.words = 100,
          random.order=FALSE, 
          rot.per=0.30, 
          use.r.layout=FALSE, 
          colors=brewer.pal(2, "Blues"))

>>>>>>> d3a2b07ccd7cdaf1c7dad1ea1c3ae2c478d2c3d5
