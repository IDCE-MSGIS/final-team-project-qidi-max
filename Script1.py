'''
# Max and Qidi
# Final Project- Web-scraping Weather Forecast
# Date: 09/23/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather    forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
# Time: 45 minutes
'''

#import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
lat = str(input('Please enter the latitude in Decimal Degrees: '))
lon = str(input('Please enter the longitude in Decimal Degrees: '))

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+'&lon='+lon
# Check if the URL exists
print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})
#removeSpaces = soup.find("li",{"class":"forecast-tombstone"}).getText(separator="\n")


# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

#
for day in forecast:
    forecast_list = day.split('\n\n')
    for M in forecast_list:
        M = M.replace('\n',':')
        M = M.replace('Night',' night')
        M = M.replace('Afternoon',' Afternoon')
        M = M.replace('High',', High')
        M = M.replace('Low',', Low')
        M = M.replace('Chance',' Chance ')
        M = M.replace('Likely',' Likely')
        M = M.replace('then',' then ')
        M = M.replace('  ',' ')
        print M.upper()
