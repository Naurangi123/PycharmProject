import yt_dlp

url = input("Enter video url..:")

ydl_opts={}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video download successfully!..")