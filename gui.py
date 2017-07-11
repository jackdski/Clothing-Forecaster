#!/usr/bin/env python

import sys
import os
#from urllib2 import urlopen
#from io import BytesIO
#from PIL import Image, ImageTk
from Tkinter import *

import weather
import declarations
import funcs

weekday = ""
for num in range(0,7):
    if num == declarations.dayOfWeek:
        weekday = declarations.weekActual[num]
print weekday

top = Tk()
top.title("Weather Program")
#top.geometry("800x500")

#path = "./images/"

avgTemp = declarations.avgTemp
print avgTemp
path = funcs.iconSelect( avgTemp )
print path

img = PhotoImage(file=path)
image = Label(top,image=img)
image.pack()

weatherText = Text(top, font='Arial')#, wrap=WORD)

#weatherLine = clearSpaces(declarations.weatherType)
weatherText.insert(INSERT, "Tommorrow on: "+declarations.currentDate +
    "\n the weather will be "+declarations.weatherType)
weatherText.pack()

repeatButton = Button(top, text="Speak", command= os.system('talk.sh'))#os.system('./talk.sh'))
repeatButton.pack()

quitButton = Button(top, text="QUIT", command=quit)
quitButton.pack()

jacket = ""      # 0 = N/A;      1 = Jacket
sleeves = ""     # 0 = short;    1 = long
pants = ""       # 0 = shorts;   1 = pants;  2 = either
footwear = ""    # 0 = shoes ;   1 = boots

funcs.clothesEvents(declarations.avgTemp)
print "Jacket: " + jacket

top.mainloop()
