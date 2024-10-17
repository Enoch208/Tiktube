import pytest
from project import download_youtube_video, download_tiktok_video

def test_download_youtube_video():

    url = "https://www.youtube.com/watch?v=BaW_jenozKc"
    assert download_youtube_video(url) is not None

def test_download_tiktok_video():

    url = "https://www.tiktok.com/@deedeeanimations/video/7421653545310637318"
    assert download_tiktok_video(url) is not None
