import tkinter as tk
from tkinter import messagebox
import numpy as np
import os
import pygame

# Initialize pygame mixer
# Use a dummy audio driver if no sound device is available
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# Note frequencies for one octave starting from middle C (C4)
NOTE_FREQUENCIES = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
}

DURATION = 0.5  # duration of each note in seconds


def generate_wave(freq, duration=DURATION, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(freq * t * 2 * np.pi)
    audio = (wave * (2**15 - 1) * volume).astype(np.int16)
    sound = pygame.sndarray.make_sound(audio)
    return sound


def generate_song(note_count):
    import random
    notes = []
    note_names = list(NOTE_FREQUENCIES.keys())
    for _ in range(note_count):
        notes.append(random.choice(note_names))
    return notes


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

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

    def generate(self):
        try:
            count = int(self.count_var.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a positive integer")
            return
        self.notes = generate_song(count)
        self.listbox.delete(0, tk.END)
        for n in self.notes:
            self.listbox.insert(tk.END, n)

    def play(self):
        if not self.notes:
            messagebox.showerror("Error", "Generate notes first")
            return
        for note in self.notes:
            freq = NOTE_FREQUENCIES[note]
            sound = generate_wave(freq)
            sound.play()
            pygame.time.wait(int(DURATION * 1000))


def main():
    root = tk.Tk()
    ComposerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
