import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pygame
import os
import random
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image, ImageTk
import io

class UltimateMediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Media Player")
        self.root.geometry("800x700")
        self.root.configure(bg="#20232a")

        # Initialize variables
        self.playlist = []
        self.current_track_index = None
        self.is_playing = False
        self.is_shuffled = False
        self.repeat_mode = 0  # 0: No repeat, 1: Repeat Track, 2: Repeat Playlist
        self.dot_count = 0

        # Initialize Pygame Mixer
        pygame.mixer.init()

        # Setup UI
        self.create_widgets()
        self.create_bindings()

    def create_widgets(self):
        # Artwork Display
        self.artwork_frame = tk.Frame(self.root, bg="#20232a", width=300, height=300)
        self.artwork_frame.pack(pady=10)
        self.artwork_label = tk.Label(self.artwork_frame, bg="#20232a")
        self.artwork_label.pack()

        # Playlist Frame
        self.playlist_frame = tk.LabelFrame(self.root, text="Playlist", bg="#20232a", fg="white", font=("Arial", 12))
        self.playlist_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(self.playlist_frame, font=("Arial", 12), selectmode=tk.SINGLE, height=10)
        self.playlist_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Track Info
        self.track_info_label = tk.Label(self.root, text="No track selected", bg="#20232a", fg="white", font=("Arial", 14))
        self.track_info_label.pack(pady=5)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Scale(self.root, variable=self.progress_var, orient="horizontal", length=600, command=self.seek_track)
        self.progress_bar.pack(pady=10)

        # Time Labels
        self.time_frame = tk.Frame(self.root, bg="#20232a")
        self.time_frame.pack(fill=tk.X, padx=20)
        self.current_time_label = tk.Label(self.time_frame, text="0:00", bg="#20232a", fg="white")
        self.current_time_label.pack(side=tk.LEFT)
        self.total_time_label = tk.Label(self.time_frame, text="0:00", bg="#20232a", fg="white")
        self.total_time_label.pack(side=tk.RIGHT)

        # Control Buttons
        self.control_frame = tk.Frame(self.root, bg="#20232a")
        self.control_frame.pack(pady=10)

        control_buttons = [
            ("Previous", self.previous_track),
            ("Play", self.play_music),
            ("Pause", self.pause_music),
            ("Next", self.next_track),
            ("Shuffle", self.toggle_shuffle),
            ("Repeat", self.toggle_repeat)
        ]

        for text, command in control_buttons:
            btn = ttk.Button(self.control_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5)

        # Volume Slider
        self.volume_frame = tk.Frame(self.root, bg="#20232a")
        self.volume_frame.pack(pady=5)
        tk.Label(self.volume_frame, text="Volume", bg="#20232a", fg="white").pack(side=tk.LEFT, padx=5)
        self.volume_slider = ttk.Scale(self.volume_frame, from_=0, to=1, orient="horizontal", length=200, command=self.set_volume)
        self.volume_slider.set(0.5)
        self.volume_slider.pack(side=tk.LEFT, padx=5)

        # File Loading
        self.load_button = ttk.Button(self.root, text="Load Files", command=self.load_files)
        self.load_button.pack(pady=10)

    def create_bindings(self):
        # Playlist double-click to play
        self.playlist_listbox.bind('<Double-1>', lambda e: self.play_music())
        
        # Keyboard shortcuts
        self.root.bind('<space>', lambda e: self.play_pause())
        self.root.bind('<Right>', lambda e: self.next_track())
        self.root.bind('<Left>', lambda e: self.previous_track())

    def load_files(self):
        files = filedialog.askopenfilenames(
            title="Select Music Files",
            filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")]
        )
        for file in files:
            self.add_to_playlist(file)

    def add_to_playlist(self, file_path):
        if file_path not in self.playlist:
            self.playlist.append(file_path)
            self.playlist_listbox.insert(tk.END, os.path.basename(file_path))
        else:
            messagebox.showinfo("Duplicate", "This file is already in the playlist.")

    def play_music(self, event=None):
        if not self.playlist:
            messagebox.showwarning("Empty Playlist", "Please add some tracks first.")
            return

        # If no track selected, start from the first track
        if self.current_track_index is None:
            self.current_track_index = 0
        elif not self.playlist_listbox.curselection():
            self.playlist_listbox.selection_set(self.current_track_index)

        file_path = self.playlist[self.current_track_index]
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Update UI
        self.is_playing = True
        self.update_track_info(file_path)
        self.update_artwork(file_path)
        self.start_progress_tracking()

    def update_track_info(self, file_path):
        try:
            audio = MP3(file_path)
            artist = audio.get("TPE1", ["Unknown Artist"])[0]
            duration = int(audio.info.length)
            
            self.track_info_label.config(
                text=f"{artist} - {os.path.basename(file_path)}"
            )
            
            # Update progress bar and time labels
            self.progress_bar.config(to=duration)
            self.total_time_label.config(text=f"{duration // 60}:{duration % 60:02d}")
        except Exception as e:
            self.track_info_label.config(text=f"Error loading metadata: {str(e)}")

    def update_artwork(self, file_path):
        try:
            audio = MP3(file_path, ID3=ID3)
            artwork = audio.get('APIC:')
            if artwork:
                image = Image.open(io.BytesIO(artwork.data))
                image = image.resize((300, 300), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.artwork_label.config(image=photo)
                self.artwork_label.image = photo
            else:
                # Default artwork or clear existing
                self.artwork_label.config(image='')
        except Exception:
            self.artwork_label.config(image='')

    def start_progress_tracking(self):
        def update_progress():
            if self.is_playing:
                current_pos = pygame.mixer.music.get_pos() // 1000
                self.progress_var.set(current_pos)
                self.current_time_label.config(text=f"{current_pos // 60}:{current_pos % 60:02d}")
                
                # Auto-advance track
                if current_pos >= self.progress_bar.cget('to'):
                    self.auto_next_track()
                
                self.root.after(1000, update_progress)
        
        update_progress()

    def auto_next_track(self):
        if self.repeat_mode == 1:  # Repeat Track
            self.play_music()
        elif self.repeat_mode == 2 or self.repeat_mode == 0:  # Repeat Playlist or No Repeat
            self.next_track()

    def pause_music(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False

    def play_pause(self):
        if self.is_playing:
            self.pause_music()
        else:
            self.play_music()

    def next_track(self):
        if not self.playlist:
            return

        # Apply shuffle if enabled
        if self.is_shuffled:
            self.current_track_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        
        self.playlist_listbox.selection_clear(0, tk.END)
        self.playlist_listbox.selection_set(self.current_track_index)
        self.play_music()

    def previous_track(self):
        if not self.playlist:
            return

        # Apply shuffle if enabled
        if self.is_shuffled:
            self.current_track_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        
        self.playlist_listbox.selection_clear(0, tk.END)
        self.playlist_listbox.selection_set(self.current_track_index)
        self.play_music()

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

    def seek_track(self, value):
        if self.playlist:
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(float(value))

    def toggle_shuffle(self):
        self.is_shuffled = not self.is_shuffled
        # Visual indication of shuffle state can be added here

    def toggle_repeat(self):
        # Cycle through repeat modes: No Repeat (0) -> Repeat Track (1) -> Repeat Playlist (2)
        self.repeat_mode = (self.repeat_mode + 1) % 3
        # Visual indication of repeat state can be added here

def main():
    root = tk.Tk()
    app = UltimateMediaPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()