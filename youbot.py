from clarifai.client import ClarifaiApi
from YouBotTwitter import YouBotStreamListener
import operator

clarifai_api = ClarifaiApi()  # assumes environment variables are set.
name = input("Enter the image url: ")
result = clarifai_api.tag_image_urls(name)

tags= result["results"][0]["result"]["tag"]["classes"]
probs= result["results"][0]["result"]["tag"]["probs"]

dictionary = dict(zip(tags, probs))

new_d = {k:dictionary[k] for k in tags if dictionary[k]>0.95}
sorted_new = sorted(new_d.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_new)

searchParameters = []

for i,j in sorted_new:
    searchParameters.append(i)

print("Searching for parameters: ", searchParameters)

streamer = YouBotStreamListener(searchParameters[0:2])

try:
    streamer.main()
except:
    streamer.print_parsed()
    pass
