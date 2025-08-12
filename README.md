<div align="center">

# 🎥 YTSage

<img src="https://github.com/user-attachments/assets/f95f7bfb-8591-4d32-b795-68e61efd670c" width="800" alt="YTSage Interface"/>

[![PyPI version](https://img.shields.io/pypi/v/ytsage?color=dc2626&style=for-the-badge&logo=pypi&logoColor=white)](https://badge.fury.io/py/ytsage)
[![License: MIT](https://img.shields.io/badge/License-MIT-374151?style=for-the-badge&logo=opensource&logoColor=white)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-1f2937?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Downloads](https://img.shields.io/pepy/dt/ytsage?color=4b5563&style=for-the-badge&label=downloads&logo=download&logoColor=white)](https://pepy.tech/project/ytsage)
[![GitHub Stars](https://img.shields.io/github/stars/oop7/YTSage?color=dc2626&style=for-the-badge&logo=github&logoColor=white)](https://github.com/oop7/YTSage/stargazers)

**A modern YouTube downloader with a clean PySide6 interface.**  
Download videos in any quality, extract audio, fetch subtitles, and more.

[Installation](#installation) •
[Features](#features) •
[Usage](#usage) •
[Screenshots](#screenshots) •
[Troubleshooting](#troubleshooting) •
[Contributing](#contributing)

</div>

---

<a id="why-ytsage"></a>

## ❓ Why YTSage?

YTSage is designed for users who want a **simple yet powerful YouTube downloader**. Unlike other tools, it offers:

- A clean, modern PySide6 interface
- One-click downloads for video, audio, and subtitles
- Advanced features like SponsorBlock, subtitle merging, and playlist selection
- Cross-platform support and easy installation

<a id="features"></a>
## ✨ Features

<div align="center">

| Core Features                     | Advanced Features                       | Extra Features                     |
|-----------------------------------|-----------------------------------------|------------------------------------|
| 🎥 Format Table                   | 🚫 SponsorBlock Integration             | 💾 Save Download Path             |
| 🎵 Audio Extraction               | 📝 Multi-Subtitle Select & Merge        | 🔄 Auto-Update yt-dlp                  |
| ✨ Simple UI                      |  💾 Save Description                    | 🛠️ FFmpeg/yt-dlp Detection         |
| 📋 Playlist Support              |  🖼️ Save thumbnail                       | ⚙️ Custom Commands                 |
| 🖼️ Playlist Selector             | 🚀 Speed Limiter                        | 🍪 Login with Cookies              |
| 📑 Embed Chapters                | ✂️ Trim Video Sections                   |                                    |

</div>



<a id="installation"></a>
## 🚀 Installation

### ⚡ Quick Install (Recommended)

Install YTSage from PyPI:

```bash
pip install ytsage
```

Then launch the app:

```bash
ytsage
```

### 📦 Pre-built Executables



- 🪟 **Windows:** `YTSage-v<version>.exe` / `YTSage-v<version>-ffmpeg.exe` (with FFmpeg)
- 🐧 **Linux:** `YTSage-v<version>-amd64.deb` / `YTSage-v<version>-x86_64.AppImage`
- 🍎 **macOS:** `YTSage-v<version>-macOS.zip` / `YTSage-v<version>.dmg`

> 👉 [Download Latest Release](https://github.com/oop7/YTSage/releases/latest)

<details>
<summary>🛠️ Manual Installation from Source</summary>

### 1. Clone the Repository

```bash
git clone https://github.com/oop7/YTSage.git
cd YTSage
```

### 2. Install Dependencies

#### ⚡ With uv

```bash
uv pip install -r requirements.txt
```

#### 📦 Or with standard pip

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

</details>

<a id="screenshots"></a>
## 📸 Screenshots

<div align="center">
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/f95f7bfb-8591-4d32-b795-68e61efd670c" alt="Main Interface" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/f7b3ebab-3054-4c77-8109-c899a8b10047" alt="Playlist Download" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><em>Main Interface</em></td>
    <td align="center"><em>Playlist Download</em></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/a80d2ae2-0031-4ed0-bee4-93293634c62a" alt="Audio Format Selection with Save Thumbnail" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/5236e3cc-8a8d-4d85-a660-782a740ef9af" alt="Subtitle Options merged with Remove Sponsor Segments" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><em>Audio Format</em></td>
    <td align="center"><em>Subtitle Options</em></td>
  </tr>
</table>
</div>

<a id="usage"></a>
## 📖 Usage

<details>
<summary>🎯 Basic Usage</summary>

1. **Launch YTSage**
2. **Paste YouTube URL** (or use "Paste URL" button)
3. **Click "Analyze"**
4. **Select Format:**
   - `Video` for video downloads
   - `Audio Only` for audio extraction
5. **Choose Options:**
   - Enable subtitles & select language
   - Enable subtitle merge
   - Save thumbnail
   - Remove sponsor segments
   - Save description
   - Embed chapters
6. **Select Output Directory**
7. **Click "Download"**

</details>

<details>
<summary>📋 Playlist Download</summary>

1. **Paste Playlist URL**
2. **Click "Analyze"**
3. **Select videos from the playlist selector (optional, defaults to all)**
4. **Choose desired format/quality**
5. **Click "Download"**

> 💡 The application automatically handles the download queue

</details>

<details>
<summary>🧰 Advanced Options</summary>

- **Quality Selection:** Choose the highest resolution for best quality
- **Subtitle Options:** Filter languages and embed into video
- **Custom Commands:** Access advanced yt-dlp features
- **Save Description:** Save the description of the video
- **Save Thumbnail:** Save the thumbnail of the video
- **Embed Chapters:** Embed chapter markers as metadata in the downloaded video file for compatible video players
- **Remove Sponsor Segments:** Remove sponsor segments from the video
- **Speed Limiter:** Limit the download speed
- **Login with Cookies:** Login to YouTube using cookies to access private content  
  How to use it:
  1. Extract cookies from your browser using an extension like [cookie-editor](https://github.com/moustachauve/cookie-editor?tab=readme-ov-file)
  2. Copy the cookies in Netscape format
  3. Create a file named `cookies.txt` and paste the cookies into it
  4. Select the `cookies.txt` file in the app
- **Save Download Path:** Save the download path
- **Update yt-dlp:** Update yt-dlp
- **FFmpeg/yt-dlp Detection:** Automatically detect FFmpeg/yt-dlp
- **Trim Video:** Download only specific parts of a video by specifying time ranges (HH:MM:SS format)


</details>

<details>
<a id="troubleshooting"></a>
<summary>🛠️ Troubleshooting</summary>

- **Format table not displaying:** Update yt-dlp to the latest version
- **Download fails:** Check your internet connection and ensure the video is available
- **Audio extraction issues:** Verify FFmpeg is properly installed

---

Configuration locations (advanced):

- Windows: `%LOCALAPPDATA%\\YTSage`
- macOS: `~/Library/Application Support/YTSage`
- Linux: `~/.local/share/YTSage`

</details>

<a id="contributing"></a>
## 👥 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch:
  ```bash
  git checkout -b feature/AmazingFeature
  ```
3. 💾 Commit your changes:
  ```bash
  git commit -m 'Add some AmazingFeature'
  ```
4. 📤 Push to the branch:
  ```bash
  git push origin feature/AmazingFeature
  ```
5. 🔄 Open a Pull Request

<details>
<summary>📂 Project Structure</summary>

# YTSage - Project Structure

This document describes the organized folder structure of YTSage.

## 📁 Project Structure

```
YTSage-main/
├── 📁 assets/                    # Static assets and resources
│   ├── 📁 Icon/                  # Application icons
│   │   └── icon.png
│   └── 📁 sound/                 # Audio files
│       └── notification.mp3
│
├── 📁 src/                       # Source code
│   ├── 📁 core/                  # Core business logic
│   │   ├── __init__.py           # Core package init
│   │   ├── ytsage_downloader.py  # Download functionality
│   │   ├── ytsage_ffmpeg.py      # FFmpeg integration
│   │   ├── ytsage_style.py       # UI styling
│   │   ├── ytsage_utils.py       # Utility functions
│   │   └── ytsage_yt_dlp.py      # yt-dlp integration
│   │
│   ├── 📁 gui/                   # User interface components
│   │   ├── 📁 dialogs/           # Dialog classes
│   │   │   ├── __init__.py       # Dialogs package init (re-exports all)
│   │   │   ├── ytsage_dialogs_base.py     # Basic dialogs (Log, About)
│   │   │   ├── ytsage_dialogs_custom.py   # Custom functionality dialogs
│   │   │   ├── ytsage_dialogs_ffmpeg.py   # FFmpeg-related dialogs
│   │   │   ├── ytsage_dialogs_selection.py # Selection dialogs
│   │   │   ├── ytsage_dialogs_settings.py  # Settings dialogs
│   │   │   └── ytsage_dialogs_update.py    # Update dialogs
│   │   │
│   │   ├── __init__.py           # GUI package init
│   │   ├── ytsage_gui_dialogs.py # Dialog aggregator (backward compatibility)
│   │   ├── ytsage_gui_format_table.py # Format table functionality
│   │   ├── ytsage_gui_main.py    # Main application window
│   │   └── ytsage_gui_video_info.py # Video information display
│   │
│   └── __init__.py               # Main package init
│
├── 📄 main.py                    # Application entry point
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # Project documentation
├── 📄 LICENSE                    # License file
└── 📄 .gitignore                 # Git ignore rules
```

</details>


## 📊 Star History

<div align="center">
  
[![Star History Chart](https://api.star-history.com/svg?repos=oop7/YTSage&type=Date)](https://star-history.com/#oop7/YTSage&Date)

</div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

<details>
<summary>Show Acknowledgments</summary>

<div align="center">

| Technology | Purpose |
|------------|---------|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Download Engine |
| [PySide6](https://wiki.qt.io/Qt_for_Python) | GUI Framework |
| [FFmpeg](https://ffmpeg.org/) | Media Processing |
| [Pillow](https://python-pillow.org/) | Image Processing |
| [requests](https://requests.readthedocs.io/) | HTTP Requests |
| [packaging](https://packaging.python.org/) | Packaging |
| [markdown](https://python-markdown.github.io/) | Markdown Processing |
| [pygame](https://www.pygame.org/) | Audio Playback |
| [loguru](https://github.com/Delgan/loguru) | Logging |
| [New Notification 09 by Universfield](https://pixabay.com/sound-effects/new-notification-09-352705/) | Notification Sound |
| [viru185](https://github.com/viru185) | Contributor |


</div>

</details>

## ⚠️ Disclaimer

This tool is for personal use only. Please respect YouTube's terms of service and content creators' rights.

---

<div align="center">

Made with ❤️ by [oop7](https://github.com/oop7)

</div>
