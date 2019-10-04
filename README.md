## Final Project Documentaion:
## Max Enger and Qidi Zhang
### National Weather Service: Five day Forecast

The file NWS_script1.py is an enhanced version of the initial script given to us that scrapes the  five day weather forecast from the National Weather Service website. The previous version of the script only extracted information about the five day forecast, but did not include any spacing or placement correction. The script we created, included the necessary correction that enable the script to print out a neater version of the five day forecast description. It was a simple job to combine knowledge from previous labs to create this script, but it still took time for us to make sure that the spacing and placement were appropriate for certain weather phenomena. Our main challenge was making sure we included the instances of the phenomena we could think of, so we could account for the corrections in the output.


### Open Weather Map

The file OWM.py utilized data from the open source platform, Open Weather Map. Open Weather Map is a small IT company out of the United Kingdom that was developed in 2014 (Open Weather Map, 2019.) The organization is comprised of engineers and big data scientists specializing in big data processing and satellite imagery processing. The main goal of the creators behind Open Weather Map was to develop and maintain efficient and easy APIs designed for their database concerning environmental phenomena and satellite imagery. There are three main APIs, the weather data, satellite imagery, and machine learning API. The second script developed in this project utilized the weather data API in order to obtain meteorological data from a certain location on the globe.


The second script was an enhanced version of a previous lab that was completed during  the course. Our goal was to enhance the previous script performance by obtaining dictionaries from the Open Weather Map open source API.  The previous script required the user to input a temperature, which was then classified as hot,  warm, cool, or cold. The enhanced version begins by gathering a location from the user (with quotation marks). This is more efficient because the user may only know the location of their whereabouts, rather than the specific temperature.  The inputted location is then used to scrape information from Open Weather Map. The script gathers more information than just the local temperature. It collects wind (speed, direction), humidity, pressure, percent cloud cover, sunset, and sunrise measurements. Those values are then printed in the console for the user to observe. Additionally, the script still classifies temperatures as hot, warm, temperate, or cold, so it will also produce that in the console. The temperature data was placed in Fahrenheit and the pressure was set to millibars, so the users in the United States could interpret the values. However, with one minor change in the scripts code the user can receive outputs in Celsius. Finally, the script reveals the time of day based on the time from sunset and sunrise. 


We both had experience in coding before, so creating the basic code structure was not the difficult part of this assignment. We found ourselves primarily relying on the API, which was detailed at the following link: https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples. 
The link allowed us to interpret which variables we could obtain and display. The challenges we faced were centered around the API calls. There are some minor bugs and little details that took time to address. For example, when first running the code, it would not work when the user inputted a location. This was frustrating because we believed we were developing the inputs appropriately. It took us about a day to figure out the the inputted location need to be in the format ‘Worcester,US’, with the quotation marks. Overall we are happy with the output and if time permitted we would have enjoyed taking this project further.




