# from pytube import YouTube
# import os
#
#
# def downloadYouTube(videourl, path):
#
#     yt = YouTube(videourl)
#     yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#
#     if not os.path.exists(path):
#         os.makedirs(path)
#     yt.download(path)
#
# downloadYouTube('https://www.youtube.com/watch?v=JLD2XWHhE7w', './videos/FindingNemo1')

from __future__ import unicode_literals
import yt_dlp


ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            # 'username': '***********@gmail.com',
            # 'password': '***********',
            # 'cookies': 'cookies.txt'
            }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # ydl.download(['https://www.youtube.com/watch?v=kkXXrRxmAyw'])
    ydl.download(['https://www.youtube.com/watch?v=JLD2XWHhE7w'])

