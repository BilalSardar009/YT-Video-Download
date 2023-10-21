# YT-Video-Download

This is a simple YouTube downloader app built with Gradio. It allows downloading YouTube videos in MP4 format or converting audio to WAV format.

## Usage
The app has a straightforward interface:
Paste any YouTube URL
Select to download as MP4 video or MP3 audio
For MP4, choose from 720p, 1080p or 2160p resolutions
Hit Submit to download
The downloaded file will be displayed for save.

## Running the app
To run the app:

```python
pip install gradio pytube ffmpeg
python app.py
```
This will launch the web interface on http://localhost:7860

## Implementation
The app is implemented in Python using following libraries:

Gradio - Creates the web interface for inputs and outputs
pytube - Downloads YouTube media
The download_youtube() function contains the main logic to fetch the video or audio stream based on user selection and download it.

Gradio converts this Python function into a web app with just a few lines of code.


## Demo
![Screenshot 2023-10-21 181401](https://github.com/BilalSardar009/YT-Video-Download/assets/94189448/e9d31443-885a-4cd0-969b-25aeb72dbd7a)
