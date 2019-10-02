# Import library and Personal API Key
import pyowm
owm = pyowm.OWM('9067d6794af11f1a696fe420647c0b95')

# Gathering Location
location = str(input("Please enter the location of the area you are interested in "
                         "(Use the following format, Worcester,US): "))
print("The location entered: ", location)


# Create Function that gathers user input as location and returns meteorological information for specified location
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

    # Sunrise time (GMT UNIXtime or ISO 8601)
    sunrise = w.get_sunrise_time('unix')  # Sunrise time (GMT UNIXtime or ISO 8601)
    # Sunset time (GMT UNIXtime or ISO 8601)
    sunset = w.get_sunset_time('unix')

    print(sunrise)

    weatherData = [wind, humidity, clouds, pressure['press']]
    # sun = [sunrise, sunset]

    # Parsing the data output from OWM to show current temperature
    t = float(temp['temp'])

    if t >= 100:
        print('According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is hot.')
    elif 70 <= t < 100:
        print('According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is warm')
    elif 32 <= t < 70:
        print('According to the most recent measurement, the temperature in ' + location + ' is:', t, ', which is temperate')
    else:
        print('According to the most recent measurement, the temperature in ' + location + 'is:', t, ', which is very cold')

    if wind in weatherData:
        print('The most recent measurements also indicate that the wind speed(mph) is: ', wind)

    if humidity in weatherData:
        print('The most recent measurements also indicate that the percent humidity is: ', humidity, '%')

    if clouds in weatherData:
        print('The most recent measurements also indicate that the percent cloud cover is: ', clouds, '%')

    if pressure in weatherData:
        print('The most recent measurements also indicate that the pressure is: ', pressure, 'mb')


weatherGather(location)
