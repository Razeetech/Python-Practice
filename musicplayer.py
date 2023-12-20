import os
import pygame
from pathlib import Path

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = self.load_playlist()
        self.current_index = 0

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
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def show_playlist(self):
        print("Current Playlist:")
        for i, song in enumerate(self.playlist):
            print(f"{i + 1}. {os.path.basename(song)}")

if __name__ == "__main__":
    music_folder = input("Enter the path to your music folder: ")
    player = MusicPlayer(music_folder)

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Stop")
        print("3. Next Track")
        print("4. Previous Track")
        print("5. Show Playlist")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            player.play()
        elif choice == "2":
            player.stop()
        elif choice == "3":
            player.next_track()
        elif choice == "4":
            player.prev_track()
        elif choice == "5":
            player.show_playlist()
        elif choice == "6":
            player.stop()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
