from subprocess import call
import time
call (["brew install bash"], shell=True)
time.sleep(1)
call (["echo '\033[1;31m This script requires brew and curl \033[0m'"], shell=True)
time.sleep(4)
call (["brew install libav"], shell=True)
call (["sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl"], shell=True)
