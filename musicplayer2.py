import os
import pygame
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root, music_folder):
        pygame.init()
        pygame.mixer.init()
        self.root = root
        self.music_folder = music_folder
        self.playlist = self.load_playlist()
        self.current_index = 0
        self.shuffle = False
        self.repeat = False

        self.create_ui()

    def load_playlist(self):
        music_files = [file for file in os.listdir(self.music_folder) if file.endswith(('.mp3', '.wav'))]
        return [str(Path(self.music_folder) / file) for file in music_files]

    def play(self, index=None):
        if index is not None:
            self.current_index = index

        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.shuffle:
            self.current_index = pygame.mixer.music.get_pos() % len(self.playlist)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def show_playlist(self):
        playlist_str = "\n".join([f"{i + 1}. {os.path.basename(song)}" for i, song in enumerate(self.playlist)])
        tk.messagebox.showinfo("Playlist", playlist_str)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        status = 'enabled' if self.shuffle else 'disabled'
        tk.messagebox.showinfo("Shuffle", f"Shuffle {status}")

    def create_ui(self):
        self.root.title("Music Player")

        play_button = tk.Button(self.root, text="Play", command=self.play)
        play_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        stop_button.pack(side=tk.LEFT, padx=5)

        next_button = tk.Button(self.root, text="Next", command=self.next_track)
        next_button.pack(side=tk.LEFT, padx=5)

        prev_button = tk.Button(self.root, text="Previous", command=self.prev_track)
        prev_button.pack(side=tk.LEFT, padx=5)

        shuffle_button = tk.Button(self.root, text="Toggle Shuffle", command=self.toggle_shuffle)
        shuffle_button.pack(side=tk.LEFT, padx=5)

        volume_label = tk.Label(self.root, text="Volume:")
        volume_label.pack(side=tk.LEFT, padx=5)

        volume_scale = tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_volume)
        volume_scale.set(0.5)  # Set default volume to 0.5
        volume_scale.pack(side=tk.LEFT, padx=5)

        playlist_button = tk.Button(self.root, text="Show Playlist", command=self.show_playlist)
        playlist_button.pack(side=tk.LEFT, padx=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        exit_button.pack(side=tk.LEFT, padx=5)

    def exit_app(self):
        self.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    music_folder = filedialog.askdirectory(title="Select Music Folder")
    player = MusicPlayer(root, music_folder)
    root.mainloop()
