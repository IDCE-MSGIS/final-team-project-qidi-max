'''
# Max and Qidi
# Final Project- Open Weather Map data collection
# Date: 10/4/2019
# The following script gathers information from the Open Weather Map open source platform by using the weather API.
# Inputs: Location Name
# Outputs: Temperature, Humidity, Wind, Pressure, Temperature classification, and time to and from sunset/sunrise
# Time: 6 hours
'''

#importing open weather map api and api key
import pyowm
owm = pyowm.OWM('9067d6794af11f1a696fe420647c0b95')

# get time
import time
timenow = time.time()

# Gathering Location
location = str(input("Please enter the location of the area you are interested in "
                     "(Use the following format, Worcester,US): "))
print("The location entered: ", location)


# Create Function that utilizes user input and returns meteorological information for a specified location
def weatherGather(location):
    # Gathering observation data from Open Weather Map
    observation = owm.weather_at_place(location)
    w = observation.get_weather()

    # Selecting specific weather details
    wind = w.get_wind()
    humidity = w.get_humidity()
    temp = w.get_temperature('fahrenheit')
    clouds = w.get_clouds()
    pressure = w.get_pressure()

    # Sunrise time
    sunrise = w.get_sunrise_time('unix')  # Sunrise time (GMT UNIXtime or ISO 8601)
    # Sunset time
    sunset = w.get_sunset_time('unix')
    tnow = int(timenow)
    tsunrise = int(sunrise)
    tsunset = int(sunrise)
    if tnow > tsunrise:
        t1 = round((float(tnow - tsunrise) / 3600), 1)
        print('It is ' + str(t1) + 'h after sunrise')
    elif tnow < tsunset and tnow > tsunrise:
        t2 = round((float(tsunset - tnow) / 3600), 1)
        print('It is ' + str(t2) + 'h before sunset')
    else:
        t3 = round((float(tnow - tsunset) / 3600), 1)
        print('It is ' + str(t3) + 'h after sunset')

    weatherData = [wind, humidity, clouds, pressure['press']]
   

    # Parsing the data output from OWM to show current temperature
    t = float(temp['temp'])

    # Assigning temperature to a condition category
    if t >= 100:
        print('According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is hot.')
    elif 70 <= t < 100:
        print('According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is warm')
    elif 32 <= t < 70:
        print(
        'According to the most recent measurement, the temperature in ' + location + ' is:', t, ', which is temperate')
    else:
        print(
        'According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is very cold')

    if wind in weatherData:
        print('The most recent measurements also indicate that the wind speed(mph) is: ', wind)

    if humidity in weatherData:
        print('The most recent measurements also indicate that the percent humidity is: ', humidity, '%')

    if clouds in weatherData:
        print('The most recent measurements also indicate that the percent cloud cover is: ', clouds, '%')

    if pressure in weatherData:
        print('The most recent measurements also indicate that the pressure is: ', pressure, 'mb')


weatherGather(location)
