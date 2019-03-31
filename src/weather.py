#!/usr/bin/python

import json
import requests
from datetime import *
from .info import *
from .funcs import *


# ID for Boulder: 5574999
# ID for San Diego County: 5391832
# ID for Poway: 5384690
def weather(info):
	url = "http://api.openweathermap.org/data/2.5/forecast?id=5574999&units=imperial&APPID=95f93c13ee33a59d9818e3e9c321791b"

	# Get data from resource
	data = requests.get(url)

	jsondata = json.loads(data.text)

	# weather_icon = jsondata["list"][3]["weather"][0]["icon"]
	# print(weather_icon)

	# Date and time
	info.date = datetime.now().strftime("%Y-%m-%d")
	day = str(int(info.date[-2:]) + 1)
	info.date = info.date[:-2] + day
	print("Date: {}".format(info.date))

	# Get day of week
	weekday_id = int(datetime.today().strftime("%w")) + 1
	info.day_of_week = get_weekday(weekday_id)
	print("Day of the Week: {}".format(info.day_of_week))
	info.day = get_weekday_actual(weekday_id)
	print("Day: {}".format(info.day))

	# collect weather data for each time point
	dt_list = [
		Timepoint(info.date + " 03:00:00"),  # 0
		Timepoint(info.date + " 06:00:00"),  # 1
		Timepoint(info.date + " 09:00:00"),  # 2
		Timepoint(info.date + " 12:00:00"),  # 3
		Timepoint(info.date + " 15:00:00"),  # 4
		Timepoint(info.date + " 18:00:00"),  # 5
		Timepoint(info.date + " 21:00:00")   # 6
	]

	# fill with data from json file
	for i in range(0, 7):
		dt_list[i].min_temp = jsondata["list"][i]["main"]['temp_min']
		dt_list[i].max_temp = jsondata["list"][i]["main"]['temp_max']
		dt_list[i].avg_temp = jsondata["list"][i]["main"]['temp']
		dt_list[i].altitude = jsondata["list"][i]["main"]['sea_level']
		dt_list[i].precipitation = jsondata["list"][i]["weather"][0]['main']
		dt_list[i].id = jsondata["list"][i]["weather"][0]['id']
		dt_list[i].description = jsondata["list"][i]["weather"][0]['description']

	precip_list = []
	for timepoint in dt_list:
		is_precip = True if timepoint.precipitation != "Clear" and timepoint.precipitation != 'Clouds' else False
		precip_list.append(tuple((timepoint.precipitation, is_precip)))

	info.precipitation = get_precip_string(precip_list)
	print("info.precipitation: ".format(info.precipitation))

	# Temperature
	min_temps = []
	max_temps = []
	avg_temps = []

	# create high, low, and avg lists excluding 3am time slot
	for timepoint in range(1, 6):
		min_temps.append(int(dt_list[timepoint].min_temp))
		max_temps.append(int(dt_list[timepoint].max_temp))
		avg_temps.append(int(dt_list[timepoint].avg_temp))

	# find min, max, and avg temps
	info.min_temp = str(min(min_temps))
	info.max_temp = str(max(max_temps))
	info.avg_temp = str(sum(avg_temps) // len(avg_temps))

	print("Max Temp: {}".format(info.max_temp))
	print("Min Temp: {}".format(info.min_temp))
	print("Avg. Temp: {}".format(info.avg_temp))

	# make clothes recommendations
	clothing_decision = "It might be  good idea to "
	clothing_decision = clothing_decision + clothes(int(info.avg_temp))

	# describe temperature
	if int(info.max_temp) > 70:
		info.weather_type = "warm weather"
	elif int(info.max_temp) in range(45, 70):
		info.weather_type = "a mild temperature"
	elif int(info.max_temp) < 45:
		info.weather_type = "cold weather"

	# describe precipitation
	if info.weatherID in range(300, 399):
		info.weather_type += "with   a  drizzle"
	elif info.weatherID in range(200, 299):
		info.weather_type += "with   a  thunderstorm"
	elif info.weatherID in range(500, 599):
		info.weather_type += "with   rain"
	elif info.weatherID in range(600, 699):
		info.weather_type += "with   snow"
	elif info.weatherID in range(801, 805):
		info.weather_type += "and cloudy"
	elif info.weatherID == 800:
		info.weather_type += "and clear skies"

	# Write to shellscript file
	weather_description = "Tomorrow  on "+ info.day + "there will be" + info.weather_type

	if info.precipitation != "clear":
		weather_description += "  and " + info.precipitation

	temp_info = "The high  is  " + info.max_temp + "   and  the  low    is   " + info.min_temp

	shellscript = open("talk.sh", "r+")
	# print("Name of shellscript: ", shellscript.name

	shellscript.truncate()  # clear file

	shellscript.write("#!/bin/bash\n")
	shellscript.write("echo \" " + weather_description + "\" | festival --tts\n")
	shellscript.write("echo \" " + temp_info + "\" | festival --tts\n")
	shellscript.write("echo \" " + clothing_decision + "\" | festival --tts\n")
	shellscript.close()
