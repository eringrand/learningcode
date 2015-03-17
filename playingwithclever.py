# Playing the with clever.com API

import requests
from collections import defaultdict

r = requests.get('https://api.clever.com/v1.1/sections', headers={'Authorization':'Bearer DEMO_TOKEN'})
response_dict = r.json()
datalist = response_dict["data"]

datadic = defaultdict(list)
for line in datalist:
	students = line["data"]["students"]
	sectionname = line["data"]["name"]
	key = sectionname
	value = students
	datadic[key].append(value)

numstudents = []
for key in datadic.iterkeys():
	x = len(datadic[key][0])
	numstudents.append(x)

print sum(numstudents)/len(numstudents)