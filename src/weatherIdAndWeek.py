# Dictionaries for weather IDs and days of week
weather = {
	#thunderstorms
		200: "a thunderstorm with light rain",
		201: "a thunderstorm with rain",
		202: "a thunderstorm with heavy rain",
		210: "a light thunderstorm",
		211: "a thunderstorm",
		212: "a heavy thunderstorm",
		221: "a ragged thunderstorm",
		230: "a thunderstorm with light drizzle",
		231: "a thunderstorm with drizzle",
		232: "a thunderstorm with heavy drizzle",

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
		800: "clear   skies",
		801: "a few    clouds",
		802: "scattered   clouds",
		803: "broken   clouds",
		804: "overcast   clouds",

	#additional
		951: "calm",
		952: "a light   breeze",
		953: "a gentle   breeze",
		954: "a moderate   breeze",
		955: "a fresh   breeze",
		956: "a strong   breeze",
		957: "a high   wind",
		958: "gale",
		959: "severe   gale",
		960: "a storm",
		961: "a violent   storm",
		962: "a hurricane"
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

# Important variables:
currentDate = ""
dayOfWeek = ""
day =  ""
weatherID = 0
precipString = ""
whenItRains = [0,0,0,0,0]
maxTemp = 0
minTemp = 0
avgTemp = 0
clothesString = ""
weatherString = ""
tempString = ""
