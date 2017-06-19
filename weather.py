#!/usr/bin/python

import json 
import requests
from datetime import *

# ID for San Diego County: 5391832
# ID for Poway: 5384690


url = "http://api.openweathermap.org/data/2.5/forecast?id=5574999&units=imperial&APPID=95f93c13ee33a59d9818e3e9c321791b"

data = requests.get(url)

jsondata = json.loads(data.text)

# Dictionaries for weather IDs and days of week
weather = {
	#thunderstorms
		200: "thunderstorm with light rain",
		201: "thunderstorm with rain",
		202: "thunderstorm with heavy rain",
		210: "light thunderstorm",
		211: "thunderstorm",
		212: "heavy thunderstorm",
		221: "ragged thunderstorm",
		230: "thunderstorm with light drizzle",
		231: "thunderstorm with drizzle",
		232: "thunderstorm with heavy drizzle",

	#drizzle
		300: "light drizzle",
		301: "drizzle",
		302: "drizzle",
		310: "drizzle",
		311: "drizzle",
		312: "drizzle",
		313: "shower rain and drizzle",
		314: "heavy shower and drizzle",
		321: "rain",

	#rain
		500: "light   rain", 
		501: "moderate   rain",
		502: "heavy   rain",
		503: "very   heavy   rain",
		504: "extreme   rain",
		511: "freezing   rain",
		520: "light   shower   rain",
		521: "shower   rain",
		522: "heavy   shower   rain",
		531: "shower   rain",

	#snow 
		600: "light   snow",
		601: "snow",
		602: "heavy   snow",
		611: "sleet",
		612: "shower   sleet",
		615: "light rain   and   snow",
		616: "rain   and   now",
		620: "light   snow",
		621: "snow",
		622: "heavy   snow",

	#atmosphere
		701: "mist",
		711: "smoke",
		721: "haze",
		731: "dust   whirls",
		741: "fog",
		751: "sand",
		761: "dust",
		762: "volcanic   ash",
		771: "squalls",
		781: "tornado",

	#sky
		800: "clear   sky",
		801: "few    clouds",
		802: "scattered   clouds",
		803: "broken   clouds",
		804: "overcast   clouds",
	
	#additional
		951: "calm",
		952: "light   breeze",
		953: "gentle   breeze",
		954: "moderate   breeze",
		955: "fresh   breeze", 
		956: "strong   breeze", 
		957: "high   wind", 
		958: "gale",
		959: "severe   gale", 
		960: "storm",
		961: "violent   storm", 
		962: "hurricane"
}

week = {
	0: "sun day",
	1: "mun day",
	2: "tews day",
	3: "wedns day",
	4: "thurs day",
	5: "fry day",
	6: "satr day"
}

# Date and time stuff

currentDate = datetime.now().strftime("%y-%m-%d")
str(currentDate)
currentDate = "20" + currentDate + " 00:00:00"
print(currentDate)

dayOfWeek = int(datetime.today().strftime("%w")) + 1
print dayOfWeek

day = ""
for place in week:
	if dayOfWeek == place: 
		day = week[place]

print day

# Weather Stuff

# weather ID
print jsondata["list"][4]["weather"][0]["id"]

# At 8pm the third index in list is noon

weatherID = jsondata["list"][3]["weather"][0]["id"]

weatherType = ""
for number in weather: 
	if weatherID == number:
		weatherType = weather[number]

#print jsondata["list"][3]

	#precip stuff
precipString = ""
#loop through the day and see if it will rain
whenItRains = [0,0,0,0,0]
for number in range(0,6):
	for id in range(200, 623):
		if id == jsondata["list"][number]["weather"][0]["id"]:
			whenItRains[number] = 1
		else: 
			whenItRains[number] = 0
#write to string if it will rain in the early morning, morning, noon, afternoon, or evening
for number in range(0,6): 
	#if 
	None


# Temperature Stuff
maxTemp = int(jsondata["list"][0]["main"]["temp_max"])
minTemp = int(jsondata["list"][0]["main"]["temp_max"])

	# go through first 6 indecies to get high and low temps 
for number in range(0,6):
	if int(jsondata["list"][number]["main"]["temp_max"]) > maxTemp:
		maxTemp = int(jsondata["list"][number]["main"]["temp_max"])

for number in range(0,6):
	if int(jsondata["list"][number]["main"]["temp_min"]) < minTemp:
		minTemp = int(jsondata["list"][number]["main"]["temp_min"])	

#maxTemp = str(jsondata["list"][4]["main"]["temp_max"]) #// 1
#minTemp = str(jsondata["list"][4]["main"]["temp_min"]) #// 1

maxTemp = str(maxTemp)
minTemp = str(minTemp)

maxTemp = maxTemp[:2]
minTemp = minTemp[:2]

print "Max Temp: " 
print maxTemp
print "Min Temp: "
print minTemp

# Write to shellscript file stuff

weatherString = "Tomorrow  on " + day + "  the weather will  be   " + weatherType
tempString = "The high  is  " + maxTemp + "   and  the  low    is   " + minTemp

shellscript = open("talk.sh", "r+") 
#print "Name of shellscript: ", shellscript.name 
	#clear file 
shellscript.truncate()

shellscript.write("#!/bin/bash\n")
shellscript.write("echo \" " + weatherString + "\" | festival --tts\n")

if len(precipString) > 0:
	shellscript.write("echo \" " + precipString + "\n | festival --tts\n")

shellscript.write("echo \" " + tempString + "\" | festival --tts\n")

shellscript.close()

