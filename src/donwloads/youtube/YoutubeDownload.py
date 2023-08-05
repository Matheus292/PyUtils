from pytube import YouTube

def download_video(url, resolution, folder=None):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_by_resolution(resolution)

    try:
        youtubeObject.download(folder)            
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred", e)