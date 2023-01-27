# Impact of Reddit WallStreetBets Forum on GME and AMC Stocks in Early 2021
Authors: Hsiao Chen Yeh, Yanying Jiang, Julien Szarata

## Project Description and Motivation

The Coronavirus pandemic shook the lives of many around the world and brought many changes to what the world
considered “normal”. While it was a very frightening time with the constant news of each country’s number of cases or
number of deaths increasing constantly, there were also plenty of new learning opportunities that arose out of this dire
situation. From the change of corporate work culture, to the sudden wave of new retail investors that began entering the
stock market, the world was changing in ways that may not have occurred without the pandemic. As Data Science
students, we wanted to apply the coursework and skills that we have cultivated during our time in this program to explore
one of the many interesting things that occurred during this time.

Our group wanted to take a look at the memestock trading frenzy that took place at the beginning of 2021 with some
names you likely heard from news sources such as GameStop and AMC Theaters.These memestocks grew in popularity
on the subreddit r/WallStreetBets where small retail investors joined forces to trigger a short squeeze2 on these stocks to
get back at the hedge funds that were shorting the stocks. Before long even news sources were talking about this subreddit
and the memestocks themselves

For this project we wanted to explore the relationship between these memstocks’ prices and the activity or chatter on
r/WallStreetBets. We wanted to know if there were any correlations between stock price and r/WallStreetBets activity. Our
goal is to tell the overall story of the short squeezes that happened in the first half of 2021. Specifically we would like to
answer the following questions:

● How did subreddit r/WallStreetBets impact the stock market?

● What were the popular memes stocks that took off in early 2021?

● When was the first major spike in the stock market that reflected the meme stock frenzy?

● How does chatter on the subreddit r/WallStreetBets react with the actual movement of the stock?

● Does high activity on reddit only happen when stock is rising or could it also happen when stock is dropping?

The following assumptions were made based on the news before we conducted our analysis.

● We assumed GameStop trader Keith Gill, known as u/DeepFuckingValue on the subreddit r/WallStreetBets was
the key player who attracted a flood of retail cash into GameStop since his reddit posts on September, 2019. We
chose this time as our starting point of investigation.

● We assumed that GameStop (GME) and AMC Theaters (AMC) would be the biggest stocks in terms of chatter or
activity on the r/WallStreetBets subreddit during the memestock craze.

## Sample Visualizations below
See here for the full report 
https://github.com/YanyingJiangUmich/Impact-of-Reddit-WallStreetBets-forum-on-GME-and-AMC-stocks-in-early-2021/blob/main/Final_Report_w_Visualizations.pdf

## When is reddit chatter most active?

We would like to explore at what time of the day is Reddit the most active. So we calculated the average count number of
posts and their comments per hour for all reddit r/wallstreetbets posts and for each of the top 2 mostly mentioned stocks,
for the period of 01/01/2021 to 04/01/2021.
![Image3](https://github.com/YanyingJiangUmich/Impact-of-Reddit-WallStreetBets-forum-on-GME-and-AMC-stocks-in-early-2021/blob/main/reddit_image3.png)

In the above visualization, we use a stacked bar highlighting activities for GME and AMC in light green and dark green
respectively. We can see that during the evenings, Reddit is much more active than during the daytime. Since Reddit is a
casual discussion forum that people are more likely to use after work, this pattern is aligned with most people’s social
media usage behavior.
We can also infer from the bar chart that the discussions on the stock GME and AMC are consistent with the overall
pattern.

## Correlation Analysis and Visualization

### GME - Reddit Mention and Stock Price Correlation Analysis

We conduct a correlation analysis to see if there is a relationship between reddit posts and the actual movement of the
stock and how strong that relationship may be for GME. We estimate the Pearson correlation coefficient to quantify the
direction and strength of the linear association between the Yahoo finance and Reddit wsb datasets.
The correlation coefficient of stock price and count of reddit mentions for GME is 0.61, indicating a positive correlation
between the two variables.

![Image1](https://github.com/YanyingJiangUmich/Impact-of-Reddit-WallStreetBets-forum-on-GME-and-AMC-stocks-in-early-2021/blob/main/reddit_image1.png)

In addition, we wanted to explore if there is any pattern embedded in the day of week. So we add color coding for each
day of week in the above scatter plot. The color pattern is pretty random according to the above plot so we don’t have any
conclusion for this.


### AMC - Reddit Mention and Stock Price Correlation Analysis
![Image2](https://github.com/YanyingJiangUmich/Impact-of-Reddit-WallStreetBets-forum-on-GME-and-AMC-stocks-in-early-2021/blob/main/reddit_image2.png)

We also do the same for AMC. The correlation coefficient of stock price and count of reddit mentions for AMC is 0.61,
indicating a positive correlation between the two variables.
Again, we are trying to find the pattern for the day of week, but we don’t see any clear relationship between the day of
week and mentions of the stock.

## Summary and Future Research Opportunities

● In this project, we have conducted various analyses to explore and visualize the relationship between stock price
change and the activities on reddit r/wallstreetbets forum. We concluded that there is positive correlation between
the two datasets, for the top 2 meme stocks GME and AMC, during the period of 01/01/2021 - 04/01/2021, when
meme stocks took off.

● During the project we had encountered a couple of challenges. The first one we faced was that the Kaggle data we
originally chose for reddit wsb mentions only has data through Aug. 2021. So we were missing a big chunk of
data for the most recent year. We ended up figuring out how to use reddit api praw and psaw to download the full
dataset for the whole subgroup r/wallstreetbets so we are able to conduct the analysis for the period we chose.

● Another challenge was that we wanted to see the correlation between yahoo finance and reddit mentions per hour.
However, Yahoo finance doesn’t provide us with hourly historical stock prices. We ended up calculating the
difference between the open and close price to support our analysis in the above section: Compare GME/AMC
Price Change to Reddit Activity.

● We also wanted to explore the impact on the stock price of an important person: Keith Gill, who started the
GameStop madness back in September 2019. According to his wikipedia, his posts under the username
“DeepFuckingValue” on Reddit were cited as a driving factor in the GameStop short squeeze of Jan. 2021 and the
subsequent trading craziness in meme stocks. However our dataset has all user info anonymized so we weren’t
able to conduct the exploration on his behaviors in an efficient way. This also creates another future research
opportunity for us after we figure out how to obtain the historical data for a specific user on Reddit.

● In the future, we would like to apply more advanced techniques using machine learning methods to conduct
predictions for meme stock spike from the reddit wsb posting activities. And we are also thinking about looking at
stock trade volumes and correlating that to mentions of reddit.
