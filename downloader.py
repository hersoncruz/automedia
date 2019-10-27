from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Download data and config

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.$(ext)s',
    'nocheckcertificate': True,
    'yesplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Songs folder
if not os.path.exists('Songs'):
    os.mkdir('Songs')
else:
    os.chdir('Songs')

# Download media
with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + argv[1], 'r') as f:
        for song_url in f:
            dl.download([song_url])
