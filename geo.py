import urllib2
import json
import sys
import csv
import time
def processAddress(address):
	formadd = address.replace(" ", "%20")
	r = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+formadd+"&sensor=false")
	
	res = json.load(r)['results']
	if len(res) == 0: 
		return json.load(r)

	lng = str(res[0]['geometry']['location']["lng"])
	lat = str(res[0]['geometry']['location']["lat"])
	nam = ""
	if len(res[0]["address_components"]) > 2:
		nam = res[0]["address_components"][2]["short_name"]
	else:
		nam = res[0]["address_components"][0]["long_name"]
	return lng + ", " + lat + ", " + nam + ', "' + address + '"'

csvinput = csv.reader(open(str(sys.argv[1]), 'rb'), delimiter=',', quotechar='"')
colIndex = csvinput.next().index("address")

allRows = (row for row in csvinput)
for row in allRows:
	print processAddress(row[colIndex])
	time.sleep(.1)