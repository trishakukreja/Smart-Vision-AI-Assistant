import webbrowser
import pyautogui
import time

def trigger_action(emotion, gesture):
    # 1. HAPPY -> PALM -> Spotify Happy Playlist
    if gesture == "Palm":
        # Direct link to a popular Happy Hits playlist
        url = "https://open.spotify.com/playlist/36IzPSaa309M1wiy9GbPrL?si=8542363d95074b4e"
        webbrowser.open_new_tab(url)
        return "Palm: Opening Happy Spotify Playlist"

    # 2. SAD -> THUMB -> YouTube Focus/Lofi
    elif gesture == "Thumb":
        url = "https://www.youtube.com/watch?v=Iv2nw3Hs4lg&list=PL7A7C47763944A32C" 
        webbrowser.open_new_tab(url)
        return "Thumb: Opening YouTube Relax Mode"

    # 3. ANGRY -> FIST -> Minimize All
    elif gesture == "Fist":
        # Minimizes all windows to show desktop
        pyautogui.hotkey('win', 'd')
        return "Fist: Privacy Mode Active"

    return None