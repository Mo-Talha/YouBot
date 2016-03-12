from clarifai.client import ClarifaiApi
import YouBotTwitter

clarifai_api = ClarifaiApi()  # assumes environment variables are set.
name = input("Enter the image url: ")
result = clarifai_api.tag_image_urls(name)

tags= result["results"][0]["result"]["tag"]["classes"]
probs= result["results"][0]["result"]["tag"]["probs"]

dictionary = dict(zip(tags,probs))

new_d = {k:dictionary[k] for k in tags if dictionary[k]>0.85}

searchParameters = []
for i in new_d:
    searchParameters.append(i)

print(searchParameters)

youbotTwitter = YouBotStreamListener()
