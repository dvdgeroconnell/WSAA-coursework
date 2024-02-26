import requests
import json
from config import config as cfg

filename = "create-file.json"
#url = 'https://api.github.com/repos/dvdgeroconnell/WSAA-restricted/contents/test'
url = 'https://api.github.com/repos/dvdgeroconnell/WSAA-restricted/contents/test/test4.py'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
# response = requests.get(url, auth = ('token', apikey))

mydata = {"message":"first commit","committer":{"name":"dvdgeroconnell","email":"dvdgeroconnell@gmail.com"},"content":"cHJpbnQoImhlbGxvIHdvcmxkIik="}

# PUT works here but POST does not. It shoulld be the other way around because
# POST is defined as post(url, data, json, args) whereas PUT is defined as put(url, data, args) - no json
# Also PUT works with "json =" but not "data ="

response = requests.put(url, json = mydata, auth = ('token', apikey))

# test4.py in base64 is cHJpbnQoImhlbGxvIHdvcmxkIik=. Converted using base64 Linux shell command
# i.e. "base64 test4.py"

# Run the program twice and you get a 422 back - "server understands your request but can't process it".
# JSON response is that "sha\" wasn't supplied - which I believe is required to modify an existing file.

print (response.status_code)
# print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
