import urllib2, urllib
import json
from BeautifulSoup import BeautifulSoup

def geocode(address):
    try:
        result = urllib2.urlopen('http://cartagen.org/utility/geocode?location=%s' % \
            urllib.quote_plus(address)).read()
        if result:
            soup = BeautifulSoup(result)
            json_response = soup.find('textarea').contents[0]
            return json.loads(json_response)
    except:
        pass