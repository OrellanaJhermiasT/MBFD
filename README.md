# Discord Music Bot

This is a music bot for Discord made in Python using **discord.py 2.0+** and **yt-dlp**.

## 🚀 Requirements
Before starting, make sure you have installed:
- Python 3.9 or higher
- FFmpeg (required to play audio)
- The libraries listed in `requirements.txt`

## 📦 Installation
1. Clone or download this repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make sure **FFmpeg** is installed and added to your PATH.

## 🔑 Token configuration
The bot uses a `.env` file to store the token securely.
- Open the `.env` file
- Replace `your token here` with your bot's actual token:
  ```env
  DISCORD_TOKEN=your_token_here
  ```
⚠️ **Never share your token**.

## ▶️ Running the bot
To start the bot:
```bash
python main.py
```

## 🎵 Available commands
- `?join` → The bot joins the voice channel you are in.
- `?disconnect` → The bot leaves the voice channel.
- `?play <URL>` → Plays music from a YouTube link.
- `?pause` → Pauses the music.
- `?resume` → Resumes the music.

## 🛠 Notes
- Make sure the bot has permissions to **connect and speak** in the voice channel.
- If audio doesn’t play, check that FFmpeg is correctly installed.

---
💡 Made with ❤️ in Python
