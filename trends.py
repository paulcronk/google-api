#Python 3

from pytrends.pyGTrends import pyGTrends
import time
from random import randint
"""
This requires the pytrends library
pip install pytrends
script source = https://github.com/GeneralMills/pytrends
caveats:
   (1) this is not supported by Google, so may stop working at any time.
   (2) there is no indication of search volumes; simply relative volumes of searches
"""
# connect to Google
google_username = "******"
google_password = "*****"
path = ""
connector = pyGTrends(google_username, google_password)

# make request to API
"""
Format is: request_report(keywords, hl='en-GB', cat=None, geo=None, date=None, gprop=None)
keywords: up to 5 keywords; seperated comma and space
cat: category??
geo: 2 letter abbreviation: "GB"
tz: timezone: "Etc/GMT+1"
date: date to start from: eg "today 7-d"
gprop: what type of search: defaults to web but "images", "news"
"""
keyword = "referendum"
connector.request_report(keyword, hl='en-GB', cat='None', geo='GB', date='today 7-d')

# wait a random amount of time between requests to avoid bot detection
time.sleep(randint(5, 10))

# download file as csv
connector.save_csv(path, "trending")

# get suggestions for keywords
keywords = "referendum"
data = connector.get_suggestions(keyword)
print(data)
