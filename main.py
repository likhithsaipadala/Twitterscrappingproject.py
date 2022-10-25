import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list1 = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:WBHomeEnt').get_items()): #declare a username
    if i>1000: #number of tweets you want to scrape
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang])
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username','url','replyCount','retweetCount','likeCount','lang'])

tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)

tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)

