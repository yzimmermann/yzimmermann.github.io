import openai
import markdown
import tweepy
import sys
import pytrends
import os

#Initialize pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)


# Authenticate with the Twitter API
consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]
openai.api_key = sys.argv[5]

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch the top trending topic
trends_response = pytrends.trending_searches()
top_trend = trends_response[0][0]
os.environ["trend_top"] = top_trend

# Use the OpenAI API to generate a piece of text on the top Twitter trend
prompt = f"Write a comprehensive article that is at least 500 words long on the topic: {top_trend}"
model = "text-davinci-003"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.5)
article_text = completions.choices[0].text

# Convert the article text to markdown format
md = markdown.markdown(article_text)

# Write the markdown text to an .md file
with open("article.md", "w") as file:
    file.write(md)

print("Article successfully generated and saved to article.md!")
