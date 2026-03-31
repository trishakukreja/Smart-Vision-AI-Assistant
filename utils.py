import os
from dotenv import load_dotenv

load_dotenv()

# Spotify Credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# UI Constants
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)