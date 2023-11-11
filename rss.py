import feedparser

# Parses RSS feed data from a URL
# TODO: Error handling
#url = 'https://w1.weather.gov/xml/current_obs/KLFI.rss'
url = input("Please enter a valid url: ")
try:
    Feed = feedparser.parse(url)
    entry = Feed.entries[0]

    print(entry.title)
except:
    print("ERROR: Invalid url")