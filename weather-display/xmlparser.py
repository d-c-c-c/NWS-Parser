from bs4 import BeautifulSoup
import requests
import lxml

#URL of the document we want to parse
url = 'https://w1.weather.gov/xml/current_obs/KLFI.xml'

document = requests.get(url)

#Parses the XML document
#Soup is the generic name for the parsing variable
soup = BeautifulSoup(document.content, "lxml-xml")

"""
Organize: Trims the data of HTML tags before returning it in JSON format
"""
def organize():
    location = soup.find("location")
    temp_f = soup.find("temp_f")
    temp_c = soup.find("temp_c")
    weather = soup.find("weather")
    relative_humidity = soup.find("relative_humidity")
    wind_dir = soup.find("wind_dir")
    wind_speed = soup.find("wind_mph")
    dewpoint = soup.find("dewpoint_string")
    visibility = soup.find("visibility_mi")
    return {
        "Location": location.get_text(),
        "TempF": temp_f.get_text(),
        "TempC": temp_c.get_text(),
        "Weather": weather.get_text(),
        "Humidity": relative_humidity.get_text(),
        "Wind Direction": wind_dir.get_text(),
        "Wind Speed": wind_speed.get_text(),
        "Dew Point": dewpoint.get_text(),
        "Visibility": visibility.get_text()
    }