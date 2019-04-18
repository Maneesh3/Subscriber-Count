import json
import urllib
#import urllib.request
#from urllib.request import urlopen, Request
import time

key = " {YOUR KEY HERE} "	# replace this key value with Youtube API key

while True:
	pew_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key=" + key
	tseries_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key=" + key
	
	pew_data = urllib.urlopen(pew_url).read()
	tseries_data = urllib.urlopen(tseries_url).read()

	#pew_data = urllib.request.urlopen(pew_url).read()
	#tseries_data = urllib.request.urlopen(tseries_url).read()
	
	pew_subs = json.loads(pew_data)["items"][0]["statistics"]["subscriberCount"]
	tseries_subs = json.loads(tseries_data)["items"][0]["statistics"]["subscriberCount"]
	#print(pew_data)
	print("PewDiePie - " + pew_subs)
	print("Tseries - " + tseries_subs)

	diff = int(pew_subs) - int(tseries_subs)
	print("Difference - "+ str(diff) + "\n")

time.sleep(1)
