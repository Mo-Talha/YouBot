import tweepy

consumer_key = "oLT41c1FVjGXrCuVEXrDtZ3vd"
consumer_secret = "ftY2n8uhzLC7eX2IdsCi9WwSKDoiqL7LPy00S33g8YTVXTZKG8"
access_token = "708674786805813248-j6INo0dAJthGhIBs9eCFZw1DCCxY8vb"
access_token_secret = "tmGwqGyvKCdoZfCjgTOyuVEORyygdiD7aoJIcjpJNsKq1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#personal_tweets = api.user_timeline(count=200)
public_tweets = api.geo_search(query="United States", granularity="country")

for tweet in public_tweets:
    if not tweet.retweeted and 'RT @' not in tweet.text and tweet.text[0] != "@":
        t = tweet.text.encode("utf-8")
        print(str(t))

'''
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
name = input("Enter the image url: ")
result = clarifai_api.tag_image_urls(name)

tags= result["results"][0]["result"]["tag"]["classes"]
probs= result["results"][0]["result"]["tag"]["probs"]


dictionary = dict(zip(tags,probs))

print(dictionary)


new_d = {k:dictionary[k] for k in tags if dictionary[k]>0.85}



print(new_d)
'''