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
    temperature = soup.find("temperature_string")
    weather = soup.find("weather")
    #print(location.get_text())
    #print(temperature.get_text())
    #print(weather.get_text())
    return {
        "Location": location.get_text(),
        "Temperature": temperature.get_text(),
        "Weather": weather.get_text()
    }