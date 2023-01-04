import openai
import markdown
import sys
import pytrends


#Initialize pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)


# Authenticate with the OpenAI API
openai.api_key = sys.argv[1]


# Fetch the top trending topic
trends_response = pytrends.trending_searches()
top_trend = trends_response[0][0]

# Use the OpenAI API to generate a piece of text on the top Twitter trend
prompt = f"Write a comprehensive article that is at least 500 words long on the topic: {top_trend}"
model = "text-davinci-003"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.5)
article_text = completions.choices[0].text

# Convert the article text to markdown format
md = markdown.markdown(article_text)

# Write the markdown text to an .md file
with open("article.md", "w") as file:
    file.write("---\n")
    file.write("layout: post\n")
    file.write(f"title: {top_trend}\n")
    file.write("---\n\n")    
    file.write(md)

print("Article successfully generated and saved to article.md!")
