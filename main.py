import openai
import markdown
import tweepy
import sys

# Authenticate with the Twitter API
consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]
openai_api_key = sys.argv[5]

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set the latitude and longitude for New York, USA
ny_lat = 40.7128
ny_long = -74.0060

# Search for tweets that contain trend hashtags within the given latitude and longitude
trends_response = api.search_tweets(query="#", geocode=f"{ny_lat},{ny_long},50km", tweet.volume_info)

# Find the trend with the highest tweet volume
top_trend = None
max_tweet_volume = 0
for trend in trends_response["trends"]:
    if trend["tweet_volume"] is not None and trend["tweet_volume"] > max_tweet_volume:
        top_trend = trend["name"]
        max_tweet_volume = trend["tweet_volume"]


# Use the OpenAI API to generate a piece of text on the top Twitter trend
prompt = f"Write an article on the top Twitter trend: {top_trend}"
model = "text-davinci-002"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.5)
article_text = completions.choices[0].text

# Convert the article text to markdown format
md = markdown.markdown(article_text)

# Write the markdown text to an .md file
with open("article.md", "w") as file:
    file.write(md)

print("Article successfully generated and saved to article.md!")
