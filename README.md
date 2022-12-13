# Effect-on-Work-Life-Balance-due-to-Covid-in-India
![Work-Life-Balance](https://user-images.githubusercontent.com/54285534/207263188-e23e910d-8ca5-43b2-ba3e-8c96f2f8549b.jpg)
## Introduction
Here we are finding out how Covid affected the Work Life Balance of people in India.

## About Data

We have scraped data from Twitter and also taken data from the IEEE dataset.

We have used scweet to scrape data from Twitter. All the data scraped is of tweets between 10 March 2020 to 23 May 2020. We have used certain hashtags to find tweets like 'WFH', 'workfromhome', 'work from home', 'workingfromhome', 'working from home', 'worklifebalance', 'work-life balance', 'worklife', 'work life' etc. In total, we were able to scrape around 28K tweets.

From the [IEEE Dataset](https://ieee-dataport.org/open-access/coronavirus-covid-19-tweets-dataset) we got 151K tweets.

## Project
- We have grouped all the relevant tweets.
- Then we extracted the tweet ids, and then the tweet ids were hydrated. So that our data is uniform.
- Afterwards, only those geotagged tweets were taken which were from India.
- Duplicate tweets are removed.
- Then, Ngrams are found for the tweet to get some sense of data.
- Topic modelling is done, and relevant topics are formed. We have used pyLDAvis for visualization.
