# install.packages("factoextra")
library(factoextra)

# Loading the data
narcData <- read.csv(paste(getwd(),"/data/clean_data/final_data_merged_storycleaned_wordcounts.csv",sep=""))
narcData <- narcData[narcData[,"Wordcount"] >= 5,]


# Factor Analysis of all data (all campaigns with some presence of any narcissism and word length >= 5)
narc.fa <- factanal(narcData[, 27:33], factors = 3, rotation = "promax")
narc.fa


# Parallel analysis to confirm the number of factors to be used
#install.packages("paran")
library(paran)
narc.pa <- paran(narcData[, 27:33], cfa = TRUE, graph = TRUE, color = TRUE,
                 col = c("black", "red", "blue"))


# Parallel Analysis shows that only one factor is to be used
narc.fa <- factanal(narcData[, 27:33], factors = 3, rotation = "promax")
narc.fa
