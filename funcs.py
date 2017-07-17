### All the functions used ###

import declarations

#finishes clothesString for clothing recommendation
def clothes(avgTemp):
	if avgTemp <= 40:
		#clothesString = " wear pants   bootz  and  several  layers"
		return " wear pants  and  several  layers"
	elif avgTemp in range(41, 55):
		return " wear pants and a sweater or jacket"
	elif avgTemp in range(55, 65):
		return " wear a sweater or jacket"
	elif avgTemp in range(65, 72):
		return " wear shorts or pants with a tee shirt"
	elif avgTemp in range(75, 80):
		return " wear  shrts   or   pants with a tee shirt"
	elif avgTemp in range(80, 85 ):
		return " wear shorts with a tee shirt"
	else:
		return " wear shorts    a tee shirt  and sandals  if appropriate"

# write to string if it will rain in the early morning, morning, noon,
# afternoon, or evening
def precipTimes(whenItRains):
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
'''
def setClothes(j,s,p,a,b,c):
	j = a
	s = b
	p = c
'''

# Decide what suggestions should be
# Not working for unknown reason
def clothesEvents(jacket, sleeves, pants):
	if declarations.avgTemp <= 40:
		#setClothes(j,s,p,"J","L","P")
		jacket = "J" #1
		sleeves = "L" #1
		pants = "P" #1   
	elif declarations.avgTemp in range(41,55):
		#setClothes(j,s,p,"J","S","P")
		jacket = "J" #1
		sleeves = "S" #0
		pants = "P" #1
	elif declarations.avgTemp in range(55, 65):
		#setClothes(j,s,p,"J","S","P/S")
		jacket = "J" #1
		sleeves = "S" #0
		pants = "P/S" #2
	elif declarations.avgTemp in range(65, 72):
		#setClothes(j,s,p,"N/A","S","P/S")
		jacket = "N/A" #0
		sleeves = "S" #0
		pants = "P/S" #2
	elif declarations.avgTemp in range(72, 80):
		#setClothes(j,s,p,"N/A","S","P/S")
		jacket = "N/A" #0
		sleeves = "S" #0
		pants = "P/S" #2
	elif declarations.avgTemp in range(80, 85 ):
		#setClothes(j,s,p,"N/A","S","S")
		jacket = "N/A" #0
		sleeves = "S" #0
		pants = "S" #0
	else:
		#setClothes(j,s,p,"N/A","S","S")
		jacket = "N/A" #0
		sleeves = "S" #0
		pants = "S" #0

	if declarations.weatherID >= 500 & declarations.weatherID < 700:
		footwear = 1
	else:
		footwear = 0


# Adds the correct extension to the url
def iconSelect(num):
	url = "./images/"
	if num in range(200,233):
		url += "11d.png"
	elif num in range(300, 322):
		url += "10d.png"
	elif num in range(500, 532):
		url += "09d.png"
	elif num in range(600, 623):
		url += "13d.png"
	elif num == 800:
		url += "01d.png"
	elif num == 801:
		url += "03d.png"
	elif num in range(802,805):
		url += "04d.png"
	else:
		url += "01d.png"
	return url

'''
def clearSpaces(line):
	line.strip(" ")
	for place in line:
		if line[place].isspace() & line[place+1].isspace():
			line = line[:place] + line[place+1:]
	return None
'''

def clearSpaces(line):
	line.strip(" ")
	'''length = len(line)
	i = 0
	while i < length:
		if line[i].isspace() & line[i+1].isspace():
			line = line[:i] + line[i+1:]
			clearSpaces(line)
		i+=1
		'''

# Important variables:
#	currentDate
#	dayOfWeek
#	day
#	weatherID
# 	precipString
#	whenItRains
#	maxTemp
#	minTemp
# 	avgTemp
# 	clothesString
# 	weatherString
# 	tempString
