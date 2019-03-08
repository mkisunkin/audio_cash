## -*- coding: utf-8 -*-
import pytube
import subprocess
import os
from memory_profiler import memory_usage
import random


link_yu = 'https://youtu.be/0srwUoIIaJg'
yt = pytube.YouTube(link_yu)


buff = yt.streams.filter(only_audio=True).first()
full_file_name = buff.default_filename 
print(full_file_name)
only_name = full_file_name[:-4]

print (only_name)


aud = yt.streams.filter(only_audio=True).first().download('c:/video')

v_filename ='C:/video/'+ full_file_name
a_filename ='C:/audio/' + only_name + '.mp3'

t_filename = random.randint(0, 10000)
t_filename = str(t_filename)


temp_v_filename = 'C:/video/'+ t_filename + '.mp4'
temp_a_filename = 'C:/audio/'+ t_filename + '.mp3'


os.rename(v_filename, temp_v_filename)


print(v_filename)
print(a_filename)
print(t_filename)
print(temp_v_filename)
print(memory_usage())
memory_usage()


command = "c:/python/python/ffmpeg/bin/ffmpeg.exe -i " + temp_v_filename + " -vn -ar 44100 -ac 2 -ab 128K -f mp3 " + temp_a_filename
print(command)
subprocess.call(command, shell=True)

os.rename(temp_a_filename, a_filename)
os.remove(temp_v_filename)
#command = "ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
print('Complete')
#ffmpeg -i source_video.avi -vn -ar 44100 -ac 2 -ab 192K -f mp3 sound.mp3
#yt.streams.get_by_itag(140).download('c:/audio')	
#aud = yt.streams.filter(only_audio=True).first().download('c:/audio')
#print (yt.streams.get_by_itag(140))

print(memory_usage())
memory_usage()