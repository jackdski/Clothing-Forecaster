# import json
# import requests

# url = "http://api.openweathermap.org/data/2.5/forecast?id=5574999&units=imperial&APPID=95f93c13ee33a59d9818e3e9c321791b"

# # Get data from resource
# data = requests.get(url)

# jsondata = json.loads(data.text)
# print(jsondata["list"][0]["dt_txt"])
# print(jsondata["list"][0]["weather"][0]['id'])
# print(jsondata["list"][0]["main"]['temp_min'])
# #print(jsondata)


mylist = [
	[1,False],
	[1,False],
	[1,False],
	[1,False]	
]

for i in mylist:
	if i[1] == 0:
		print('false')