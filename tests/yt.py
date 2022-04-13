from HackerGprat import basic as b
from pytube import YouTube
import os

def yt_download(videourl, path="./Output"):

    b.clear()
    # b.upgradePIP()
    print("Connecting...")
    
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if not os.path.exists(path):
        print("Creating Folder...")
        os.makedirs(path)

    print("Downloading...")
    yt.download(path)
    print("SucessFully Downloaded...")

url = 'https://www.youtube.com/watch?v=U4ogK0MIzqk&ab_channel=SebastianLague'
yt_download( url )

# urls = []

# for i in urls:
#     yt_download(i)
