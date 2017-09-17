#!/usr/bin/env python

import sys
import os
from Tkinter import *

import weather
import declarations
import funcs

weekday = ""
for num in range(0,7):
    if num == declarations.dayOfWeek:
        weekday = declarations.weekActual[num]
print weekday

# What the weather forcast is
weatherString = declarations.weatherType
weatherString[0].capitalize()
#funcs.clearSpaces(weatherString)


gui = Tk()
gui.title("Weather Program")
gui.geometry("550x350")

avgTemp = declarations.avgTemp
print avgTemp

# Create path to get icons for gui
path = os.getcwd() 
extention = funcs.iconSelect( declarations.weatherID )
path = path.replace("src", "Images/")
path = path + extention
#print path

img = PhotoImage(file=path)#, height=50, width=50)
image = Label(gui,image=img)
image.pack()

weatherText = Text(gui, font='Arial')#, wrap=WORD)

weatherText.insert(INSERT, "\t\t\t"+weekday+" "+declarations.currentDate)
weatherText.insert(INSERT, "\n\t\t    the weather will be "+weatherString)
weatherText.pack()

weatherText.insert(INSERT, "\n\n\t\tHigh:\t\t\tLow:")
weatherText.insert(INSERT, "\n\t\t"+declarations.maxTemp+
	"\t\t\t"+declarations.minTemp)


jacket = ""      # 0 = N/A;      1 = Jacket
sleeves = ""     # 0 = short;    1 = long
pants = ""       # 0 = shorts;   1 = pants;  2 = either
footwear = ""    # 0 = shoes ;   1 = boots

#funcs.clothesEvents(jacket, sleeves, pants)

if declarations.avgTemp <= 40:
	#setClothes(j,s,p,"J","L","P")
	jacket = "Jacket" #1
	sleeves = "Long" #1
	pants = "Pants" #1   
elif declarations.avgTemp in range(41,55):
	#setClothes(j,s,p,"J","S","P")
	jacket = "Jacket" #1
	sleeves = "Short" #0
	pants = "Pants" #1
elif declarations.avgTemp in range(55, 65):
	#setClothes(j,s,p,"J","S","P/S")
	jacket = "Jacket" #1
	sleeves = "Short" #0
	pants = "Pants/Shorts" #2
elif declarations.avgTemp in range(65, 72):
	#setClothes(j,s,p,"N/A","S","P/S")
	jacket = "N/A" #0
	sleeves = "Short" #0
	pants = "Pants/Shorts" #2
elif declarations.avgTemp in range(72, 80):
	#setClothes(j,s,p,"N/A","S","P/S")
	jacket = "N/A" #0
	sleeves = "Shorts" #0
	pants = "Pants/Shortss" #2
elif declarations.avgTemp in range(80, 85 ):
	#setClothes(j,s,p,"N/A","S","S")
	jacket = "N/A" #0
	sleeves = "Short" #0
	pants = "Shorts" #0
else:
	#setClothes(j,s,p,"N/A","S","S")
	jacket = "N/A" #0
	sleeves = "Short" #0
	pants = "Shorts" #0

if declarations.weatherID >= 500 & declarations.weatherID < 700:
	footwear = "Sandals"
else:
	footwear = "Boots"

print "Jacket: "
print jacket

weatherText.insert(INSERT, "\n\nJacket:\t\tSleeves:\t\tPants:\t\tFootwear:")

weatherText.insert(INSERT, "\n\n"+jacket)
weatherText.insert(INSERT, "\t\t"+sleeves)
weatherText.insert(INSERT, "\t\t"+pants)
weatherText.insert(INSERT, "\t\t"+footwear)

weatherText.pack()

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

#quitButton = Button(gui, text="QUIT", command=quit)
#quitButton.pack()


gui.mainloop()
