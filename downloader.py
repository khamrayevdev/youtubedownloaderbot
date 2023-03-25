from pytube import YouTube
from moviepy.editor import VideoFileClip


hd1080 = 137
hd720 = 22
hd360 = 18


def highest(url):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(hd1080)
    stream.download()
    filename = stream.default_filename
    return filename

def norm(url):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(hd720)
    stream.download()
    filename = stream.default_filename
    # return filename

def second(url):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(hd360)
    stream.download()
    global filename
    filename = stream.default_filename
    # print(filename)


def get_audio(url):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(18)
    stream.download()
    filename = stream.default_filename
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    endfilename = filename[:-4] + 'mp3'
    clip.close()
    # return endfilename


# second('https://www.youtube.com/watch?v=tWoo8i_VkvI')
