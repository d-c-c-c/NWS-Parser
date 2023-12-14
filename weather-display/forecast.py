import openmeteo_requests
import requests_cache
import numpy as np
import pandas as pd
import math
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)



"""
Helper functions for data
"""
"""
Takes in a degree value and returns the bearing as would be seen on a compass.
"""
def degreesToCompassBearing(num) -> str:
    DIRECTIONS = ['↑ N', '↗ NE', '→ E', '↘ SE', '↓ S', '↙ SW', '← W', '↖ NW']
    bearing = math.floor((num / 45) + 0.5)
    return DIRECTIONS[bearing % 8]

"""
Changes the temperature data from Fahrenheit to Celsius
"""
def toCelsius(temp) -> int:
    return (temp - 32) * 5/9

"""
Converts feet to miles
"""
def toMiles(distance) -> int:
    return distance * 0.000189394
"""
Trims the decimal values off of the forecast data
"""
def trimDecimals(data):
    for i in range(len(data)):
        value = int(data[i])
        data[i] = value
    return data

"""
Formats the decimal places of the desired list

data: the data being input
position: the desired position to round to
"""
def formatDecimals(data, position):
    for i in range(len(data)):
        value = round(data[i], position)
        data[i] = value
    return data


# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 37.0299,
	"longitude": -76.3452,
	"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "visibility", "wind_speed_10m", "wind_direction_10m"],
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max"],
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"timezone": "America/New_York",
	"forecast_days": 10
}
responses = openmeteo.weather_api(url, params=params)


# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_visibility = hourly.Variables(3).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(4).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(5).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["dew_point_2m"] = hourly_dew_point_2m
hourly_data["visibility"] = hourly_visibility
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
# Contains the compass bearing for the wind direction from hourly data
wind_bearing = []
# Hourly temperature in Celsius
temperature_c = []
# Hourly visibility in miles
visibility_mi = []
#rewriting wind direction data to show compass bearing rather than degrees
for i in range(len(hourly_data["wind_direction_10m"])):
    wind_bearing.append(degreesToCompassBearing(hourly_data["wind_direction_10m"][i]))

for i in range(len(hourly_data["temperature_2m"])):
    temperature_c.append(toCelsius(hourly_data["temperature_2m"][i]))
    
for i in range(len(hourly_data["visibility"])):
	visibility_mi.append(toMiles(hourly_data["visibility"][i]))
    
#TODO: Implement weather code info. Maybe change function in weathericons.py to be more generalized
#TODO: Geocoding nonsense for location
hourly_dataframe = pd.DataFrame(data = hourly_data)
#print(hourly_dataframe)

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(3).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s"),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["weather_code"] = daily_weather_code
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max



