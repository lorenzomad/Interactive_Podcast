import pytest

from podcast.podcast import Podcast


podcast = Podcast("Lorenzo")

def test_podcast_creation():
    """tests podcast creation"""
    assert podcast.topic == None