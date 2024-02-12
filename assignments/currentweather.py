# currentweather.py
# Program to print out the current temperature on the console
# Topic 02 Assignment
# Author : David O'Connell
# Reference(s):
#    Andrew Beatty - WSAA2.4 Consuming JSON with Python (video lecture)
#    Open Meteo API Documentation: https://open-meteo.com/en/docs/
# ---------------------------------------------------------------------

# import the required modules
# import json is not required as we are not using any of the methods

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=53.2&longitude=-9.1&current=temperature_2m,wind_direction_10m"

# get the contents of the web page above

response = requests.get(url)

# load the retrieved json into a dictionary object called "data"

data = response.json()

# Now look into the dictionary object for the required fields - temperature and wind direction

# Temperature
temperature = data['current']['temperature_2m']
temp_units = data['current_units']['temperature_2m']
print(f"The current air temperature at your co-ordinates at 2m above the ground is {temperature}{temp_units}")

# Wind direction (per Open Meteo documentation referenced above)
wind_direction = data['current']['wind_direction_10m']
wind_units = data['current_units']['wind_direction_10m']
print(f"The current wind direction at your co-ordinates at 10m above the ground is {wind_direction}{wind_units}")
