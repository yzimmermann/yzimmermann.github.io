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

# Get the WOEID for New York, USA
places_response = api.trends_available()
ny_woeid = None
for place in places_response:
    if place["name"] == "New York":
        ny_woeid = place["woeid"]
        break

# Fetch the top Twitter trend in New York, USA
trends = api.trends_place(ny_woeid)
trends_list = trends[0]["trends"]
top_trend = trends_list[0]["name"]

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
