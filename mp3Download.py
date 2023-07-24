import click
from pytube import YouTube
import os

@click.command()
@click.option("--url", prompt="Enter URL", help="The URL of the video")

def download(url):
    try:
        video = YouTube(url)

        print('Title: ', video.title)
        print('Downloading.... ')

        out_path = video.streams.filter(only_audio=True).first().download()

        new_name = os.path.splitext(out_path)

        os.rename(out_path, new_name[0] + '.mp3')

        print("Done.")
    
    except:
        print("Failure")
        pass

if __name__ == "__main__":
    download()
