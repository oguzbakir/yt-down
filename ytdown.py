from subprocess import call
import time
import os
file = open("urls.txt","r")
if os.path.getsize('urls.txt') == 0:
	print ("Please enter valid url's to urls.txt")
else:
	call (["echo '\033[1;31m This script requires brew \033[0m'"], shell=True)
	time.sleep(1)
	call (["brew install bash"], shell=True)
	call (["brew install libav"], shell=True)
	call (["brew install youtube-dl"], shell=True)
	for line in file.readlines():
		my="youtube-dl -x --audio-format mp3 "+liste
		call ([my], shell=True)
	file.close()