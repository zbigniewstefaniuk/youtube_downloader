import os
import glob

from pydub import AudioSegment
from pytube import YouTube

SONGS_PATH = './Music From Youtube'             # Path where the songs are located


def youtube_downloader():
    """
    :return: this script return song
    """
    yt_link = YouTube(input('URL: '))           # Getting song url
    print('processing...')
    song = yt_link.streams.last()               # selecting *webm format for best audio quality
    song_title = yt_link.title                  # getting title for song
    print(f'Downloading "{song_title}" - in progress...')
    song.download(SONGS_PATH)
    print('\nDownloading is complete\n')


youtube_downloader()

def converter_to_audio():
    extension_list = ('*.webm', '*.flv')        # files with this extension will be selected

    os.chdir(SONGS_PATH)                        
    for extension in extension_list:
        print('Processing songs...')
        for video in glob.glob(extension):
            mp3_filename = os.path.splitext(
                os.path.basename(video))[0] + '.mp3'
            AudioSegment.from_file(video).export(mp3_filename,
                                                 format='mp3',
                                                 bitrate="256k",)
    print('Downloaded !')

converter_to_audio()

def del_files():
    print('program start')
    entries = os.listdir('Music From Youtube/')
    for all_files in entries:
        splited_txt = all_files.split(' ')
        reversed_txt = splited_txt[::-1]
        getting_extension = reversed_txt[1:3].split('.')
        print(getting_extension)
        print(reversed_txt[1])


# del_files()
