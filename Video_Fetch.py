import pytube
from pytube import Search
from pytube import YouTube
import sys
import os
import subprocess

from pytube.request import stream

#Give options to user to pull video, or a collection of videos from a playlist
# target = input('Input a URL of the video you want converted: ')


#Upon fetch, using stream, indicate progress
def progressFunc(stream, chunk, bytesRem):
    print(bytesRem)

#Take videos and convert them to .mp3 files
"""
def completedFunc(stream, filepath):
    #Run conversion on completetion
    #Possibly async conversions
"""

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
    
    
    return selectedStream

try:
    # testUrl = 'https://www.youtube.com/watch?v=Zj-M9pvQSyo'
    testUrl = input("FEED ME A YOUTUBE URL:")
    yt = YouTube(testUrl)

    #yt.register_on_progress_callback(progressFunc)
    #yt.streams.filter(only_audio=True)

    selectedStream = GetVideoInfo(testUrl)
    
    # itag = yt.streams.filter(res="144p").first().itag
    # stream = yt.streams.get_by_itag(itag)
    path = selectedStream.download('Downloads')
    # print(path)
    
    #Conversion
    #https://www.ffmpeg.org
    subprocess.run([
        'ffmpeg',
        '-i',
        path,
        (path + ".mp3")
    ])
    

    #Delete videos once completed for memory  
except:
    print(sys.exc_info())
