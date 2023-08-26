from pytube import YouTube
import os

def download_video(url, resolution, folder=None):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_by_resolution(resolution)

    try:
        youtubeObject.download(folder)            
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred", e)

def download_audio(url, folder=None):
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()

    if folder is None:
        folder = '.'

    try: 
        out_file = video.download(output_path=folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(youtube.title + " has been successfully downloaded.")
    except Exception as e:
        print("An error has occured", e)