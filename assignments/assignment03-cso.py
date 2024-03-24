# assignment03-cso.py
# Topic 04 assignment

# Program to retrieve the dataset for the "exchequer account (historical series)" from the CSO
# and store it in a file called "cso.json".

# Author(s): David O'Connell

# Reference(s):
#    Andrew Beatty - WSAA4.2, WSAA4.3: Reading data via APIs from data.gov.ie and CSO.ie
#    CSO's PxStat Open Data Platform: https://data.cso.ie/product/FI, https://data.cso.ie/table/FIQ02
# -----------------------------------------------------------------------------------------------------

# Import the modules for handling HTTP requests / responses and JSON data
import requests, json

# URL for required data set
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# GET and extract the data
response = requests.get(url)
result = response.json()

#print(result)

# Save the data to a file called "cso.json"
with open("cso.json",'w') as file:
    json.dump(result, file, indent=4)

# Tidy up
file.close()

#json_string = json.dumps(result)
#print(f"string is {json_string}")