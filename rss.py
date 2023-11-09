import feedparser

# Parses RSS feed data from a URL

# TODO: Error handling
Feed = feedparser.parse('https://w1.weather.gov/xml/current_obs/KLFI.rss')

entry = Feed.entries

print(entry)