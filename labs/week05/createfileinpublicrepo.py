# This program tests if it possible to create a file in a public repo without authentication.

import requests
import json
from config import config as cfg

filename = "create-file2.json"
url = 'https://api.github.com/repos/dvdgeroconnell/WSAA-coursework/contents/labs/assignment04.txt'


# The auth token is required because you can only read from public repositories without an auth key.
apikey = cfg["courseworkkey"]

# First get the file

response = requests.get(url, auth = ('token', apikey))


'''

mydata = {"message":"commit w/o key","committer":{"name":"dvdgeroconnell","email":"dvdgeroconnell@gmail.com"},"content":"cHJpbnQoImhlbGxvIHdvcmxkIik="}

# PUT works here but POST does not. It should be the other way around because
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

    '''