#!/usr/bin/python

import json
import requests
from datetime import *

import declarations
import funcs

# ID for Boulder: 5574999
# ID for San Diego County: 5391832
# ID for Poway: 5384690


url = "http://api.openweathermap.org/data/2.5/forecast?id=5574999&units=imperial&APPID=95f93c13ee33a59d9818e3e9c321791b"

# Get data from resource
data = requests.get(url)

jsondata = json.loads(data.text)

weatherIcon = jsondata["list"][3]["weather"][0]["icon"]
print weatherIcon

# Date and time 

declarations.currentDate = datetime.now().strftime("%y-%m-%d")
str(declarations.currentDate)
declarations.currentDate = "20" + declarations.currentDate #+ " 00:00:00"
print "Date:"
print declarations.currentDate

# Get day of week
declarations.dayOfWeek = int(datetime.today().strftime("%w")) + 1
print "Day of the Week:"
print declarations.dayOfWeek

for place in declarations.week:
	if declarations.dayOfWeek == place:
		declarations.day = declarations.week[place]
print "Day:"
print declarations.day

# Weather 

# weather ID
#print jsondata["list"][4]["weather"][0]["id"]
# At 8pm the third index in list is noon the next day
declarations.weatherID = jsondata["list"][3]["weather"][0]["id"]
print "Weather ID:"
print declarations.weatherID

for number in declarations.weather:
	if declarations.weatherID == number:
		declarations.weatherType = declarations.weather[number]

#print jsondata["list"][3]

#precip 
#loop through the day and see if it will rain
declarations.whenItRains = [0,0,0,0,0]
for number in range(0,5):
	for value in range(200, 623):
		if value == jsondata["list"][number]["weather"][0]["id"]:
			declarations.whenItRains[number] = 1

print "When It Will Rain:"
print declarations.whenItRains


declarations.precipString = funcs.precipTimes(declarations.whenItRains)
#print precipString

# Temperature 
declarations.maxTemp = int(jsondata["list"][0]["main"]["temp_max"])
declarations.minTemp = int(jsondata["list"][0]["main"]["temp_max"])

# go through first 6 indecies to get high and low temps
for number in range(0,6):
	if int(jsondata["list"][number]["main"]["temp_max"]) > declarations.maxTemp:
		declarations.maxTemp = int(jsondata["list"][number]["main"]["temp_max"])

for number in range(0,6):
	if int(jsondata["list"][number]["main"]["temp_min"]) < declarations.minTemp:
		declarations.minTemp = int(jsondata["list"][number]["main"]["temp_min"])

#maxTemp = str(jsondata["list"][4]["main"]["temp_max"]) #// 1
#minTemp = str(jsondata["list"][4]["main"]["temp_min"]) #// 1

# Find the average temperature
declarations.avgTemp = (declarations.maxTemp + declarations.minTemp) / 2

declarations.maxTemp = str(declarations.maxTemp)
declarations.minTemp = str(declarations.minTemp)

declarations.maxTemp = declarations.maxTemp[:2]
declarations.minTemp = declarations.minTemp[:2]

print "Max Temp: "
print declarations.maxTemp
print "Min Temp: "
print declarations.minTemp

# make clothes recommendations
clothesString = "It might be  good idea to "
clothesString = clothesString + funcs.clothes(declarations.avgTemp)


# Write to shellscript file
weatherString = "Tomorrow  on "+declarations.day+"  the weather will  be   "
	+ declarations.weatherType + "  and " + declarations.precipString
tempString = "The high  is  " + declarations.maxTemp + "   and  the  low    is   " + declarations.minTemp

shellscript = open("talk.sh", "r+")
#print "Name of shellscript: ", shellscript.name

shellscript.truncate()	#clear file

shellscript.write("#!/bin/bash\n")
shellscript.write("echo \" " + weatherString + "\" | festival --tts\n")
shellscript.write("echo \" " + tempString + "\" | festival --tts\n")
shellscript.write("echo \" " + clothesString + "\" | festival --tts\n")
shellscript.close()
