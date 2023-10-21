import gradio as gr
import pytube 

def download_youtube(url, choice, res):

  yt = pytube.YouTube(url)

  if choice == 'mp3':
    audio = yt.streams.filter(only_audio=True).first()
    print(f"Downloading {audio.title} as MP3")
    return audio.download(),audio.download(), None

  elif choice == 'mp4':
    if res == "720p":
      video = yt.streams.filter(res="720p").first()
    elif res == "1080p":  
      video = yt.streams.filter(res="1080p").first()
    elif res == "2160p":
      video = yt.streams.filter(res="2160p").first()
    else:
      return "Invalid resolution"
    
    print(f"Downloading {video.title} at {video.resolution}")
    return video.download(),None,video.download()

  else:
    return "Invalid choice"

choice_options = ["mp3", "mp4"]
resolution_options = ["720p", "1080p", "2160p"]

iface = gr.Interface(fn=download_youtube, 
         inputs=["text", 
                gr.Radio(choices=choice_options),
                gr.Radio(choices=resolution_options)],
         outputs=[gr.File(),gr.Audio(),gr.Video()])

iface.launch()
