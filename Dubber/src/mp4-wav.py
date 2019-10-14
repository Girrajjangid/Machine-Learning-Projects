import subprocess

command = "ffmpeg -i ../video/sample.webm -ab 160k -ac 2 -ar 44100 -vn ../audio/sample.wav"

subprocess.call(command, shell=True)