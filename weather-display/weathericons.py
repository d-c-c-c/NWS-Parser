import openmeteo_requests
from datetime import datetime
# Setting up Open-Meteo API client
openmeteo = openmeteo_requests.Client()

# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 37.0299,
	"longitude": -76.3452,
	"current": "weather_code",
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"timezone": "America/New_York"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_weather_code = current.Variables(0).Value()

#print(f"Current weather_code {current_weather_code}")


'''
Icon match: Checks  the current weather code value and returns the name of the appropriate icon
'''
def iconMatch(weatherCode):
    if weatherCode == 0:            #Clear skies
        return '01d'
    elif weatherCode == 1:          #Mainly clear
        return '02d'
    elif weatherCode == 2:          #Partly Cloudy
        return '03d'
    elif weatherCode == 3:          #Overcast
        return '04d'
    elif 45 <= weatherCode <= 48:   #Fog
        return '50d'
    elif 51 <= weatherCode <= 57:   #Drizzle or Freezing Drizzle
        return '09d'
    elif (61 <= weatherCode <= 67) or (80 <= weatherCode <=82):   #Rain or Freezing rain
        return '10d'
    elif (71 <= weatherCode <= 77) or (85 <= weatherCode <= 86):   #Snowfall of any kind
        return '13d'
    elif 95 <= weatherCode <= 99:   #Thunderstorms of any kind
        return '11d'
    else:                           #Unknown weather set as default
        return 'unknown'
    
"""
TODO Write a short description for this function

"""
def checkIfNight(curTime, iconStr):
    # If it is currently NIGHT && iconStr != unknown, replace the d in the icon name with and n for the nighttime icon 
    if (iconStr != 'unknown') and (curTime >= 18 or curTime <= 6):
        updatedIconStr = iconStr.replace(iconStr[2], 'n')
        return updatedIconStr
    # If it is current DAY && iconStr != unknown,  return the unchanged string
    elif (iconStr != 'unknown') and (6 <= curTime <= 18):
        return iconStr
    else:
        return 'unknown'

    # It is currently daytime, do nothing
        
