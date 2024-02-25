# converts a web page to a pdf 
# This is to demonstrate API Keys
# Author: Andrew Beatty


import requests
import urllib.parse

from config import config as cfg

targetUrl = "https://en.wikipedia.org"

apikey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

#wb opens the file in binary mode as we are not writing text.
with open("document.pdf", "wb") as handler:
    handler.write(result)

