# This program tests that you can read the content of a public repo without authentication

import requests
import json
from config import config as cfg

results_file = "WSAA-coursework.json"
url = 'https://api.github.com/repos/dvdgeroconnell/WSAA-coursework/contents/labs'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

#apikey = cfg["githubkey"]
#response = requests.get(url, auth = ('token', apikey))

response = requests.get(url)

print (response.status_code)
#print (response.json())

with  open(results_file, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
