#!/usr/bin/env python

import sys
import os
from tkinter import *

from .info import *
from .funcs import *


def gui(info):
	# What the weather forecast is
	weather_string = info.weather_type
	weather_string.capitalize()
	# funcs.clearSpaces(weather_string)

	my_gui = Tk()
	my_gui.title("Weather Program")
	my_gui.geometry("550x350")

	avg_temp = info.avg_temp

	# Create path to get icons for gui
	path = os.getcwd()
	extention = icon_select(info.weatherID)
	path += '/Images/' + extention
	print("path: {}".format(path))

	img = PhotoImage(file=path)  # , height=50, width=50)
	image = Label(my_gui, image=img)
	image.pack()

	weather_text = Text(my_gui, font='Arial')  # , wrap=WORD)

	weather_text.insert(INSERT, "\t\t\t" + info.day + " " + str(info.date))

	weather_text.insert(INSERT, "\n\t\t    the weather will be " + weather_string)
	weather_text.pack()

	weather_text.insert(INSERT, "\n\n\t\tHigh:\t\t\tLow:")
	weather_text.insert(INSERT, "\n\t\t" + info.max_temp + "\t\t\t" + info.min_temp)

	jacket = ""      # 0 = N/A;      1 = Jacket
	sleeves = ""     # 0 = short;    1 = long
	pants = ""       # 0 = shorts;   1 = pants;  2 = either
	footwear = ""    # 0 = shoes ;   1 = boots

	# funcs.clothesEvents(jacket, sleeves, pants)

	if int(info.avg_temp) <= 40:
		jacket = "Jacket"
		sleeves = "Long"
		pants = "Pants"
	elif int(info.avg_temp) in range(41,55):
		# setClothes(j,s,p,"J","S","P")
		jacket = "Jacket"
		sleeves = "Short"
		pants = "Pants"
	elif int(info.avg_temp) in range(55, 65):
		# setClothes(j,s,p,"J","S","P/S")
		jacket = "Jacket"
		sleeves = "Short"
		pants = "Pants/Shorts"
	elif int(info.avg_temp) in range(65, 72):
		# setClothes(j,s,p,"N/A","S","P/S")
		jacket = "N/A"
		sleeves = "Short"
		pants = "Pants/Shorts"
	elif int(info.avg_temp) in range(72, 80):
		# setClothes(j,s,p,"N/A","S","P/S")
		jacket = "N/A"
		sleeves = "Shorts"
		pants = "Pants/Shorts"
	elif int(info.avg_temp) in range(80, 85):
		# setClothes(j,s,p,"N/A","S","S")
		jacket = "N/A"
		sleeves = "Short"
		pants = "Shorts"
	else:
		# setClothes(j,s,p,"N/A","S","S")
		jacket = "N/A"
		sleeves = "Short"
		pants = "Shorts"

	# if raining or snowing wear boots
	if info.weatherID >= 500 & info.weatherID < 700:
		footwear = "Boots"
	# otherwise wear what you want
	else:
		footwear = "Tennis Shoes or Sandals"

	weather_text.insert(INSERT, "\n\nJacket:\t\tSleeves:\t\tPants:\t\tFootwear:")

	weather_text.insert(INSERT, "\n\n" + jacket)
	weather_text.insert(INSERT, "\t\t" + sleeves)
	weather_text.insert(INSERT, "\t\t" + pants)
	weather_text.insert(INSERT, "\t\t" + footwear)

	weather_text.pack()

	'''
	jacketText = Text(gui, font='Arial', width=5 bd=5)
	jacketText.insert(INSERT, jacket)
	jacketText.pack()
	
	sleevesText = Text(gui, font='Arial', bd=5)
	sleevesText.insert(INSERT, sleeves)
	sleevesText.pack()
	
	pantsText = Text(gui, font='Arial', bd=50)
	pantsText.insert(INSERT, pants)
	pantsText.pack()
	
	footwearText = Text(gui, font='Arial', bd=50)
	footwearText.insert(INSERT, footwear)
	footwearText.pack()
	'''

	# quitButton = Button(gui, text="QUIT", command=quit)
	# quitButton.pack()

	my_gui.mainloop()
