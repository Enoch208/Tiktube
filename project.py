from __future__ import unicode_literals
import yt_dlp
import os
import time
import pyfiglet

def display_welcome():
    welcome_message = pyfiglet.figlet_format("Tiktube 🎥")
    print(welcome_message)
    print("Welcome to the Tiktube Downloader!")
    print("You can download videos from YouTube and TikTok.\n")

def download_youtube_video(video_url, save_path='downloads'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
    }

    try:
        print(f"Downloading YouTube video from URL: {video_url}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            return filename

    except Exception as e:
        return f"Oops! An error occurred while downloading: {str(e)}"

def download_tiktok_video(video_url, save_path='downloads'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
    }

    try:
        print(f"Downloading TikTok video from URL: {video_url}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            return filename

    except Exception as e:
        return f"Oops! An error occurred while downloading: {str(e)}"

def main():
    display_welcome()
    while True:
        video_url = input("Enter the video URL (YouTube or TikTok), or 'q' to quit: ")
        if video_url.lower() == 'q':
            print("Thanks for using Tiktube! Goodbye! 👋")
            break

        print(f"Checking URL: {video_url} - Status Code: 200")

        if "youtube.com" in video_url or "youtu.be" in video_url:
            print("Detected platform: YouTube")
            filename = download_youtube_video(video_url)

        elif "tiktok.com" in video_url:
            print("Detected platform: TikTok")
            filename = download_tiktok_video(video_url)

        else:
            print("Unsupported URL. Please enter a valid YouTube or TikTok URL.")
            continue

        if isinstance(filename, str) and filename.startswith("Oops!"):
            print(filename)
        else:
            print(f"🎉 Download complete! Please check '{filename}' for your video.\n")

if __name__ == "__main__":
    main()
