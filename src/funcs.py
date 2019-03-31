# finishes clothing recommendation
def clothes(avg_Temp):
	if avg_Temp <= 40:
		# clothesString = " wear pants   bootz  and  several  layers"
		return " wear pants  and  several  layers"
	elif avg_Temp in range(41, 55):
		return " wear pants and a sweater or jacket"
	elif avg_Temp in range(55, 65):
		return " wear a sweater or jacket"
	elif avg_Temp in range(65, 72):
		return " wear shorts or pants with a tee shirt"
	elif avg_Temp in range(75, 80):
		return " wear  shrts   or   pants with a tee shirt"
	elif avg_Temp in range(80, 85):
		return " wear shorts with a tee shirt"
	else:
		return " wear shorts    a tee shirt  and sandals  if appropriate"


# write to string if it will rain in the early morning, morning, noon,
# afternoon, or evening
# todo: implement getting a time range of when it will precipitate
# def get_precip_weight(precip_times):
	# weight = [0] * len(precip_times)
	# for i in range(0, len(precip_times)):
	# 	if precip_times[i][1] is True:
	# 		weight[i] += 1
	# 		j = i
	# 		for j in range(i, len(precip_times)):
	# 			if precip_times[j][1] is True:
	# 				weight += 1
	# 				j += 1
	# 			else:
	# 				break
	#
	# start_time = max(weight)
	# for i in weight:
	# 	if i == start_time:
	# 		position = i
	# 	else:
	# 		position = -1
	#
	# print("Longest weight: {}".format(start_time))
	#
	# highest_weight = max(weight)

def get_precip_string(precip_times):
	will_precip = False
	precip_type = "no"

	for i in range(0, len(precip_times)):
		print(precip_times[i][1])
		if precip_times[i][1] is True:
				print("trUe")
				will_precip = True
				precip_type = precip_times[i][0]
				break

	if will_precip:
		if precip_type == "Snow":
			return "it will snow"
		elif precip_type == "Rain":
			return "it will rain"
		else:
			precip_type = "none"
		return precip_type
	else:
		return "clear"


'''
def setClothes(j,s,p,a,b,c):
	j = a
	s = b
	p = c
'''


# # Decide what suggestions should be made
# # Not working
# def clothes_events(info, jacket, sleeves, pants):
# 	if info.avg_Temp <= 40:
# 		jacket = "J"  # 1
# 		sleeves = "L"  # 1
# 		pants = "P"  # 1
# 	elif info.avg_Temp in range(41,55):
# 		jacket = "J"  # 1
# 		sleeves = "S"  # 0
# 		pants = "P"  # 1
# 	elif info.avg_Temp in range(55, 65):
# 		jacket = "J"  # 1
# 		sleeves = "S"  # 0
# 		pants = "P/S"  # 2
# 	elif info.avg_Temp in range(65, 72):
# 		jacket = "N/A"  # 0
# 		sleeves = "S"  # 0
# 		pants = "P/S"  # 2
# 	elif info.avg_Temp in range(72, 80):
# 		jacket = "N/A"  # 0
# 		sleeves = "S"  # 0
# 		pants = "P/S"  # 2
# 	elif info.avg_Temp in range(80, 85 ):
# 		jacket = "N/A"  # 0
# 		sleeves = "S"  # 0
# 		pants = "S"  # 0
# 	else:
# 		jacket = "N/A"  # 0
# 		sleeves = "S"  # 0
# 		pants = "S"  # 0
#
# 	if info.weatherID >= 500 & info.weatherID < 700:
# 		footwear = 1
# 	else:
# 		footwear = 0


# Adds the correct extension to the url
def icon_select(num):
	url = ""
	if num in range(200, 233):
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
	elif num in range(802, 805):
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