import streamlit as st
import subprocess
import os
import sys

st.set_page_config(page_title="AI Vision Workspace", layout="wide")

# Custom CSS for UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1e1e2f, #2a2a40);
        color: white;
    }
    .stButton>button {
        background-color: #6200ea !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 22px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Next-Gen Vision AI Assistant")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🎮 Interaction Guide:
    * ✋ **Show Palm** → 🟢 **HAPPY MODE** (Opens Spotify)
    * 👍 **Thumb Up** → 🔵 **SAD MODE** (Opens YouTube)
    * ✊ **Make Fist** → 🔴 **ANGRY MODE** (Minimizes All)
    """)
    
    if st.button("🚀 LAUNCH AI ASSISTANT"):
        st.info("Starting Camera System... Please check your taskbar.")
        venv_python = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")
        if not os.path.exists(venv_python):
            venv_python = "python"
        subprocess.Popen([venv_python, "app.py"])

with col2:
    st.markdown("### 🔗 Quick Access")
    st.markdown("[![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com)")
    st.write("")
    st.markdown("[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com)")

st.markdown("---")
