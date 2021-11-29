import pytube
from pytube import Search
from pytube import YouTube
import sys
import os
import subprocess
import re
from pytube.request import stream

#Upon fetch, using stream, indicate progress
def progressFunc(stream, chunk, bytesRem):
    print(bytesRem)

#DASH = Audio and video codec seperate
#Progressive = Audio and video together 

def GetVideoInfo (Video):    
    vid = YouTube(Video)
    selectedStream = "None"
    print(vid.title)
    if(len(vid.streams.filter(is_dash=True)) > 0):
        print("Has DASH")
        if(len(vid.streams.filter(only_audio=True)) > 0):
            print("Found Audio only stream")
            selectedStream = vid.streams.filter(is_dash=True,only_audio=True).first()

    elif(len(vid.streams.filter(progressive=True)) > 0):
        print("Has Progressive")
        if(len(vid.streams.filter(progressive=True)) > 0):
            print("Found Audio only stream")
            selectedStream = vid.streams.filter(is_progressive=True).first()
    return selectedStream

def TrimName(videoName):
    newName = re.sub(".mp4", "", videoName)
    return newName

try:
    
    ytUrl = input("FEED ME A YOUTUBE URL:")
    yt = YouTube(ytUrl)

    selectedStream = GetVideoInfo(ytUrl)
    
    path = selectedStream.download('Downloads')
    
    #Cleaning off the .mp4
    os.rename(path, TrimName(path))
    path = TrimName(path)
    
    #Conversion
    #https://www.ffmpeg.org
    subprocess.run([
        'ffmpeg',
        '-i',
        path,
        (path + ".mp3")
    ])
    
    #Delete videos once completed for memory
    os.remove(path)  
except:
    print(sys.exc_info())
