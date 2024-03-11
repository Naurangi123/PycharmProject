from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
import random

root = Tk()


class MusicPlayer:
    root.configure(bg='#fcfcec')
    root.minsize(500, 600)
    root.maxsize(500, 600)

    def __init__(self, window):
        def des():
            mixer.music.stop()
            root.destroy()

        window.title('Universal Music Player')
        window.resizable(0, 0)
        Play = Button(window, text='Play', width=10, command=self.play, bg='#4b7fa4', fg="#fcfcec", font=("times", 20))
        Pause = Button(window, text='Pause', width=10, command=self.pause, bg='#4b7fa4', fg="#fcfcec",
                       font=("times", 20))
        Stop = Button(window, text='Stop', width=10, command=self.stop, bg='#cb464e', fg="#fcfcec", font=("times", 20))
        Random = Button(window, text='ChangeSong', width=10, command=self.random, bg='#4b7fa4', fg="#fcfcec", font=("times", 20))
        Close = Button(window, text='Close', width=10, command=des, bg='#cb464e', fg="#fcfcec", font=("times", 20))
        Random.place(x=0, y=20)
        Play.place(x=150, y=20)
        Pause.place(x=300, y=20)
        Stop.place(x=0, y=75)
        Close.place(x=150, y=75)
        self.music_file = False
        self.playing_state = False

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

    def random(self):
        music_dir = 'D:\music'  # Replace with your directory path
        music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3') or f.endswith('.wav')]
        if music_files:
            self.music_file = os.path.join(music_dir, random.choice(music_files))
            self.play()


app = MusicPlayer(root)
root.mainloop()
