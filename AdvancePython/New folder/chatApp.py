import random
from datetime import datetime as dt
import os
greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","please tell me date", "date", "today's date"]
timeIntent = ["what's the time","please tell me time", "time", "current time"]
songsIntent = ["play song", "music", "play music", "song"]
videoIntent=["play movie","movie","video","play video"]

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in greetIntent:
        ans = random.choice(greetIntent)
        print(ans.title())
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%H:%M:%S, %p"))
    elif msg in songsIntent:
        songs_dir = r"D:\music"
        songs_list = os.listdir(songs_dir)
        song = random.choice(songs_list)
        song_path = songs_dir + "/" + song
        os.startfile(song_path)
    elif msg in videoIntent:
        videos_dir = r"D:\Movies\Uncharted.2022.720p.BluRay.H264.AAC-RARBG"
        videos_list = os.listdir(videos_dir)
        video = random.choice(videos_list)
        videos_path = videos_dir + "/" + video
        os.startfile(videos_path)
    elif msg == "bye":
        print("Bye..Take Care")
        break
    else:
        print("I don't understand...")