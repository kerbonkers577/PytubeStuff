import pytube
from pytube import Search
from pytube import YouTube
import sys
from pathlib import Path

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
    # print(vid.title)
    print(vid.streams.filter(is_dash=True, res="144p").first())
    # print("Thumbnail: " + yt.thumbnail_url)

try:
    url = 'https://www.youtube.com/watch?v=E0wRCNIerEo'
    yt = YouTube(url)

    #yt.register_on_progress_callback(progressFunc)
    #yt.streams.filter(only_audio=True)

    # GetVideoInfo(url)
    
    itag = yt.streams.filter(is_dash=True, res="144p").first().itag
    
    stream = yt.streams.get_by_itag(itag)
    stream.download('Downloads')

    #Conversion
    #https://www.ffmpeg.org


    #Delete videos once completed for memory  
except:
    print(sys.exc_info())
