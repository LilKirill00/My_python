from __future__ import unicode_literals
import yt_dlp

from youtube_transcript_api import YouTubeTranscriptApi
import csv
import json


def get_transcript_subtitle(video, dst: str = "dst"):
    try:
        video_id = video.replace('https:', '').replace('www.', '').replace('youtube.com', '').replace('watch?v=', '').replace('/', '').replace(' ', '')

        trance = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru'], cookies='www.youtube.com_cookies.txt')

        with open("result/"+dst+".csv", 'w', encoding="utf-8", newline="") as file:
            dstwriter = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            i = 0
            while i < len(trance):
                tmp = json.dumps(trance[i])
                tmp = json.loads(tmp)
                dstwriter.writerow([tmp['start'], tmp['text']])
                i = i + 1
    except:
        print("неправльная ссылка", video_id, dst)
        return 0


def get_other_metode(URL):
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'json3',
        'subtitleslangs': ['ru'],
        'skip_download': True,
        # 'username': '*******@gmail.com',
        # 'password': '***********',
        'cookies': 'cookies.txt'
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URL)


if __name__ == '__main__':
    # video1 = "https://www.youtube.com/watch?v=bYzGwfdjc-A"
    # get_transcript_subtitle(video1)
    # get_transcript_subtitle("IMsUJol_TRk")
    get_other_metode('https://www.youtube.com/watch?v=JLD2XWHhE7w')