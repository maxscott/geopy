import urllib2
import json
import sys

address = sys.argv[1].replace(" ", "%20w")
r = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+address+"&sensor=false")
print(json.load(r)['results'][0]['geometry']['location'])