#!/usr/bin/python

import json
import requests
from datetime import *

import weatherIdAndWeek

# ID for San Diego County: 5391832
# ID for Poway: 5384690


url = "http://api.openweathermap.org/data/2.5/forecast?id=5574999&units=imperial&APPID=95f93c13ee33a59d9818e3e9c321791b"

data = requests.get(url)

jsondata = json.loads(data.text)

###   Functions   ###

#finishes clothesString for clothing recommendation
def clothes():
	if avgTemp <= 40:
		#clothesString = " wear pants   bootz  and  several  layers"
		return " wear pants   bootz  and  several  layers"
	elif avgTemp in range(41, 55):
		return " wear pants and a sweater or jacket"
	elif avgTemp in range(56, 65):
		return " wear a sweater or jacket"
	elif avgTemp in range(66, 72):
		return " wear shorts or pants with a tee shirt"
	elif avgTemp in range(73, 80):
		return " wear  shrts   or   pants with a tee shirt"
	elif avgTemp in range(81, 85 ):
		return " wear shorts with a tee shirt"
	else:
		return " wear shorts    a tee shirt  and sandals  if appropriate"
# write to string if it will rain in the early morning, morning, noon,
# afternoon, or evening
def precipTimes():
	if whenItRains == [0,0,1,1,1]:
		return "will continue from noon on"
	elif whenItRains == [0,0,0,1,1]:
		return "will start in the evening"
	elif whenItRains == [1,1,0,0,0]:
		return "only in the morning"
	elif whenItRains == [0,1,1,1,0]:
		return "only in the middle of the day"
	elif whenItRains == [0,1,1,0,0]:
		return "in the late morning"
	elif whenItRains == [0,0,0,0,0]:
		return "clear all day"
	elif whenItRains == [1,1,1,1,1]:
		return "all day"
	elif whenItRains == [1,0,0,0,0]:
		return "in the early morning"
	elif whenItRains == [0,0,0,0,1]:
		return "at night "
	else :
		return "scattered"




# Date and time stuff

currentDate = datetime.now().strftime("%y-%m-%d")
str(currentDate)
currentDate = "20" + currentDate + " 00:00:00"
print "Date:"
print currentDate

dayOfWeek = int(datetime.today().strftime("%w")) + 1
print "Day of the Week:"
print dayOfWeek

day = ""
for place in weatherIdAndWeek.week:
	if dayOfWeek == place:
		day = weatherIdAndWeek.week[place]
print "Day:"
print day

# Weather Stuff

# weather ID
print "Weather ID:"
print jsondata["list"][4]["weather"][0]["id"]

# At 8pm the third index in list is noon

weatherID = jsondata["list"][3]["weather"][0]["id"]

weatherType = ""
for number in weatherIdAndWeek.weather:
	if weatherID == number:
		weatherType = weatherIdAndWeek.weather[number]

#print jsondata["list"][3]

	#precip stuff
precipString = ""
#loop through the day and see if it will rain
whenItRains = [0,0,0,0,0]
for number in range(0,6):
	for id in range(200, 623):
		if id == jsondata["list"][number]["weather"][0]["id"]:
			whenItRains[number] = 1
print "When It Will Rain:"
print whenItRains

precipString = precipTimes()
#print precipString

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

avgTemp = (maxTemp + minTemp) / 2

maxTemp = str(maxTemp)
minTemp = str(minTemp)


maxTemp = maxTemp[:2]
minTemp = minTemp[:2]

print "Max Temp: "
print maxTemp
print "Min Temp: "
print minTemp

# make clothes recommendations
clothesString = "It might be  good idea to "
clothesString = clothesString + clothes()

#print clothesString

# Write to shellscript file stuff

weatherString = "Tomorrow  on " + day + "  the weather will  be   " + weatherType + "and " + precipString
tempString = "The high  is  " + maxTemp + "   and  the  low    is   " + minTemp

shellscript = open("talk.sh", "r+")
#print "Name of shellscript: ", shellscript.name
	#clear file
shellscript.truncate()

shellscript.write("#!/bin/bash\n")
shellscript.write("echo \" " + weatherString + "\" | festival --tts\n")
shellscript.write("echo \" " + tempString + "\" | festival --tts\n")
shellscript.write("echo \" " + clothesString + "\" | festival --tts\n")
shellscript.close()
