import urllib2
import json
import sys
import csv

inp = open(str(sys.argv[1]), 'rb')
csvinput = csv.reader(inp, delimiter=',', quotechar='"')
col = csvinput.next().index("address")

def processAddress(address):
	formadd = address.replace(" ", "%20")
	r = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+formadd+"&sensor=false")
	
	res = json.load(r)['results']
	
	lng = str(res[0]['geometry']['location']["lng"])
	lat = str(res[0]['geometry']['location']["lat"])
	nam = ""
	if len(res[0]["address_components"]) > 2:
		nam = res[0]["address_components"][2]["short_name"]
	else:
		nam = res[0]["address_components"][0]["long_name"]
	return lng + ", " + lat + ", " + nam + ', "' + address + '"'

for row in csvinput:
	print processAddress(row[col])