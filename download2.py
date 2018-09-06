from __future__ import unicode_literals
import youtube_dl, sys

if (len(sys.argv) < 2):
    print("Link empty!")
    sys.exit(0) 

link = sys.argv[1]
link2 = 'https://www.youtube.com/watch?v=dP15zlyra3c'

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
