import openmeteo_requests
import requests_cache
import numpy as np
import pandas as pd


# Setup the Open-Meteo API client 

openmeteo = openmeteo_requests.Client()

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 37.0299,
	"longitude": -76.3452,
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max"],
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"timezone": "America/New_York"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

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

# if __name__ == '__main__':
#     print(trimDecimals(daily_data['weather_code'].tolist()))
#     print(formatDecimals(daily_data['temperature_2m_max'].tolist(),1))
#     print(formatDecimals(daily_data['temperature_2m_min'].tolist(),1))
#     print(formatDecimals(daily_data['wind_speed_10m_max'].tolist(),1))


