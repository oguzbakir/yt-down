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
	k = int(input("1-Mp4\n2-Mp3\nSelect One : "))
	if k == 2:
		for line in file.readlines():
			my="youtube-dl -x --audio-format mp3 "+line
			call ([my], shell=True)
	if k == 1:
		for line in file.readlines():
			my="youtube-dl "+line
			call ([my], shell=True)
	file.close()
