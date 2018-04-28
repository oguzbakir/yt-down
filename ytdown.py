import os
import platform
import sys
from subprocess import call

file = open("urls.txt", "r")
if os.path.getsize('urls.txt') == 0:
    print ("Please enter valid url's to urls.txt")
    sys.exit(0)

if platform.system() == "Darwin":
    call(["echo '\033[1;31m This script requires brew \033[0m'"], shell=True)
    call(["brew install bash", "brew install libav", "brew install youtube-dl"], shell=True)

if platform.system() == "Linux":
    call(["sudo apt-get install youtube-dl"], shell=True)

if platform.system() == "Windows":
    print("Fuck you i don't support windows")

k = int(input("1-Mp4\n2-Mp3\nSelect One : "))
if k == 2:
    for line in file.readlines():
        my = "youtube-dl -x --no-check-certificate --audio-format mp3 " + line
        call([my], shell=True)
if k == 1:
    for line in file.readlines():
        my = "youtube-dl --no-check-certificate " + line
        call([my], shell=True)
file.close()
