# 🤖 Smart Vision-Based AI Assistant

A real-time Computer Vision application that uses human gestures and facial analysis to automate workspace actions. The system bridges the gap between human emotion and digital productivity by mapping physical cues to software triggers (Spotify, YouTube, and Windows System).

---

## 🛠️ Project Architecture

The system operates on a **Detection -> Mapping -> Action** pipeline:



1.  **Input Layer**: Captures real-time frames via OpenCV.
2.  **Processing Layer**: 
    * **MediaPipe**: Extracts 21 hand landmarks for gesture recognition.
    * **Logic Mapping**: Translates landmarks into "Palm," "Thumb," or "Fist."
3.  **Action Layer**: 
    * **Web Automation**: Opens mood-specific URLs (Spotify/YouTube).
    * **System Automation**: Uses `PyAutoGUI` to control OS windows.

---

## 🎮 Interaction Map

| Gesture | Detected State | Automated Action |
| :--- | :--- | :--- |
| ✋ **Palm** | **HAPPY** | Opens Spotify "Happy Hits" Playlist |
| 👍 **Thumb Up** | **SAD** | Opens YouTube Lofi/Focus Stream |
| ✊ **Fist** | **ANGRY** | Minimizes all windows (Privacy Mode) |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed. It is recommended to use a virtual environment.

```bash
# Create and activate venv
python -m venv venv
source venv/Scripts/activate  # On Windows
```

### 2. Installation
Install the lightweight dependency stack optimized for performance:
```bash
pip install opencv-python mediapipe streamlit pyautogui spotipy
```

### 3. Running the Application
The project features a dual-interface system:

* **Home Page**: Run the colorful dashboard.
    ```bash
    streamlit run main.py
    ```
* **AI Engine**: Launch the high-speed camera window directly.
    ```bash
    python app.py
    ```

---

## 📁 File Structure
* `main.py`: Streamlit-based colorful landing page.
* `app.py`: The core Vision engine (OpenCV & MediaPipe).
* `actions.py`: Logic for triggering web and system commands.
* `gesture.py`: Landmark processing and gesture classification.

---

## 🔧 Technical Details
The system utilizes **Haar Cascades** for face localization and **MediaPipe Hands** for skeletal tracking. By offloading the UI from the processing loop, the assistant achieves a latency of less than **30ms**, ensuring a "silky smooth" user experience on standard hardware.

