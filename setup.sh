# setup.sh 
# Author: Jack Danielski

# Program that implements a daily task so that the Clothing Forecaster runs at 8pm

# Important: switch path in cronfile.txt to where you saved main.sh

# Set cronjob for 8pm, when the program is optimized for accuracy
echo "Add cronjob? This will run the Clothing Forecaster everyday at 8pm"
echo "Y or N?"

read answer

if [ "$answer" == "Y" ] || [ "$answer" == "y" ]; then
	#crontab /home/jack/Desktop/Clothing-Forecaster-master/cronfile.txt
	echo "Cron task added"
		echo "0 20 * * * /home/jack/Desktop/Clothing-Forecaster-master/main.sh" >> crontab -e
elif [ "$answer" == "N" ] || [ "$answer" == "n" ]; then 
	echo "Cron task NOT added"
else 
	echo "Error: Answer was not Y or N. Try again"
fi

# Festival Text-To-Speech Command Line Download
echo "Install Festival Text-To-Speech? This enables the program to speak when being used"
echo "Y or N?"

read tts

if [ "$tts" == "Y" ] || [ "$tts" == "y" ]; then
	sudo apt-get install festival 
	echo "Festival Text-To-Speech added"
elif [ "$tts" == "N" ] || [ "$tts" == "n" ]; then 
	echo "Festival Text-To-Speech NOT added"
else 
	echo "Error: Answer was not Y or N. Try again"
fi

exit
