import tkinter as tk
from tkinter import messagebox
import numpy as np
import os
import pygame
import random

import music_theory as mt

# Initialize pygame mixer
# Use a dummy audio driver if no sound device is available
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# Default beats per minute
DEFAULT_BPM = 90


def generate_wave(frequencies, duration, volume=0.5):
    """Create a pygame Sound for a list of frequencies."""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.zeros_like(t)
    for freq in frequencies:
        wave += np.sin(freq * t * 2 * np.pi)
    wave /= max(len(frequencies), 1)
    audio = (wave * (2**15 - 1) * volume).astype(np.int16)
    sound = pygame.sndarray.make_sound(audio)
    return sound


def generate_melody(note_count, start_note="mC"):
    """Generate a melody using interval rules from the C++ implementation."""
    melody = [start_note]
    current = start_note
    for _ in range(note_count - 1):
        direction = random.choice(["up", "down"])
        if direction == "up":
            choices = mt.melody_interval_up(current)
        else:
            choices = mt.melody_interval_down(current)
        if choices:
            current = random.choice(choices)[1]
        melody.append(current)
    return melody


class ComposerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Auto Song Composer")
        self.notes = []

        self.count_label = tk.Label(master, text="Number of Notes:")
        self.count_label.pack()

        self.count_var = tk.IntVar(value=8)
        self.count_entry = tk.Entry(master, textvariable=self.count_var)
        self.count_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate)
        self.generate_button.pack()

        self.bpm_label = tk.Label(master, text="Tempo (BPM):")
        self.bpm_label.pack()
        self.bpm_var = tk.IntVar(value=DEFAULT_BPM)
        self.bpm_scale = tk.Scale(master, from_=60, to=140, orient=tk.HORIZONTAL, variable=self.bpm_var)
        self.bpm_scale.pack()

        self.listbox = tk.Listbox(master, width=20)
        self.listbox.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.is_playing = False

    def generate(self):
        try:
            count = int(self.count_var.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a positive integer")
            return
        self.notes = generate_melody(count)
        self.listbox.delete(0, tk.END)
        for note in self.notes:
            self.listbox.insert(tk.END, note)

    def play(self):
        if not self.notes:
            messagebox.showerror("Error", "Generate notes first")
            return
        self.is_playing = True
        bpm = self.bpm_var.get()
        for note in self.notes:
            if not self.is_playing:
                break
            freq = mt.note_to_frequency(note)
            duration = 60 / bpm
            sound = generate_wave([freq], duration)
            sound.play()
            pygame.time.wait(int(duration * 1000))

    def stop(self):
        self.is_playing = False


def main():
    root = tk.Tk()
    ComposerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
