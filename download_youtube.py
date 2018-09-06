#! /usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : Download youtube
    @date: 20180906
"""
from pytube import YouTube
import sys
import threading, time

if (len(sys.argv) < 2):
    print("Link empty!")
    sys.exit(0) 

link = sys.argv[1]

save_path = "./"
link2 = 'https://www.youtube.com/watch?v=OGS1sGhGsOs'

try:
    yt = YouTube(link)
except:
    print("Connection Error")

# ### yt.streams.all()
# print("===== yt.streams.all()")
# for i in yt.streams.all():
#     print(i)

# ### yt.streams.filter(progressive=True).all()
# print("===== yt.streams.filter(progressive=True).all()")
# for i in yt.streams.filter(progressive=True).all():
#     print(i)

# ### yt.streams.filter(adaptive=True).all()
# print("===== yt.streams.filter(adaptive=True).all()")
# for i in yt.streams.filter(adaptive=True).all():
#     print(i)

# print("===== yt.streams.get_by_itag(18)")
# print(yt.streams.get_by_itag(18))

print("===== list video")
listVideo = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().all()
for i in listVideo:
    print(i)

indexSelected = input("select index [0 - {0}]: ".format(len(listVideo) - 1))
if (indexSelected == ""):
    indexSelected = 0

## progress
file_size = 0
def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    percent = (100 * (file_size - bytes_remaining) / file_size)
    print("\rBytes remaining: {0}KB [{1:.1f}% downloaded]".format(bytes_remaining / 1000, percent), end="")
    sys.stdout.flush()
yt.register_on_progress_callback(show_progress_bar)

down_video = listVideo[int(indexSelected)]
print("Downloading... ", down_video)

file_size = down_video.filesize
print("file_size: {0}KB".format(file_size / 1000))

try:    
    print("===== Downloading... ")
    down_video.download(save_path)
    print("\nxong.hehe")
except:
    print("\nSome Error!")
