piano = ["#B/mC", "#C/bD", "mD", "#D/bE", "bF/mE", "#E/mF", "#F/bG", "mG", "#G/bA", "mA", "#A/bB", "bC/mB", "#B/mC"]
intervals = [
    {0: "P1", 1: "A1"},
    {0: "D2", 1: "m2", 2: "M2", 3: "A2"},
    {2: "D3", 3: "m3", 4: "M3", 5: "A3"},
    {4: "D4", 5: "P4", 6: "A4"},
    {6: "D5", 7: "P5", 8: "A5"},
    {7: "D6", 8: "m6", 9: "M6", 10: "A6"},
    {9: "D7", 10: "m7", 11: "M7", 12: "A7"},
    {11: "D8", 12: "P8"},
]
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
test = ["#B", "mC", "#C", "bD", "mD", "#D", "bE", "bF", "mE", "#E", "mF", "#F", "bG", "mG", "#G", "bA", "mA", "#A", "bB", "bC", "mB", "#B", "mC"]
melody_intervals = [
    "P1",
    "A1",
    "D2",
    "m2",
    "M2",
    "A2",
    "D3",
    "m3",
    "M3",
    "A3",
    "P4",
    "P5",
]

NOTE_TO_SEMITONE = {
    "#B":0, "mC":0,
    "#C":1, "bD":1,
    "mD":2,
    "#D":3, "bE":3,
    "bF":4, "mE":4,
    "#E":5, "mF":5,
    "#F":6, "bG":6,
    "mG":7,
    "#G":8, "bA":8,
    "mA":9,
    "#A":10, "bB":10,
    "bC":11, "mB":11,
}
BASE_FREQ = 261.63  # frequency of middle C (mC)

from math import pow

def note_to_frequency(note: str) -> float:
    octave = 0
    if note.startswith('+'):
        octave = 1
        note = note[1:]
    elif note.startswith('-'):
        octave = -1
        note = note[1:]
    semitone = NOTE_TO_SEMITONE.get(note)
    if semitone is None:
        raise ValueError(f"Unknown note {note}")
    return BASE_FREQ * pow(2, octave) * pow(2, semitone / 12)

def _strip_octave(note: str) -> str:
    """Return the base note without octave prefix."""
    if note.startswith(('+', '-')):
        return note[1:]
    return note


def two_pitch_position_solver(low: str, high: str):
    low = _strip_octave(low)
    high = _strip_octave(high)
    loop_count = len(piano)
    low_where = high_where = None
    flag = 0
    for i in range(loop_count):
        key = piano[i]
        if key[0] in '#b':
            notes_in_key = [key[:2], key[3:]]
        else:
            notes_in_key = [key]
        if low_where is None and low in notes_in_key:
            low_where = i
            flag += 1
        if high_where is None and high in notes_in_key:
            high_where = i
            flag += 1
        if flag == 2:
            break
    if high_where < low_where:
        return low_where, high_where + loop_count - 1
    return low_where, high_where

def two_pitch_distance_solver(low: str, high: str) -> int:
    low = _strip_octave(low)
    high = _strip_octave(high)
    low_where = notes.index(low[1])
    high_where = notes.index(high[1])
    loop_count = len(notes)
    if high_where < low_where:
        return (high_where + loop_count + 1) - low_where
    return (high_where - low_where) + 1

def interval_solver(low: str, high: str) -> str:
    low_p, high_p = two_pitch_position_solver(low, high)
    distance = two_pitch_distance_solver(low, high)
    distance_k = high_p - low_p
    try:
        return intervals[distance-1][distance_k]
    except KeyError:
        return "Error"

def high_pitch_solver(low: str, interval: str) -> str:
    for t in test:
        if interval == interval_solver(low, t):
            return t
    if interval == "P8":
        return '+' + low
    return "None"

def low_pitch_solver(high: str, interval: str) -> str:
    for t in test:
        if interval == interval_solver(t, high):
            return t
    if interval == "P8":
        return '-' + high
    return "None"

def pitch_solver(pitch: str, interval: str):
    return (low_pitch_solver(pitch, interval), high_pitch_solver(pitch, interval))

def melody_interval_up(pitch: str):
    pitches = []
    for interval in melody_intervals:
        val = high_pitch_solver(pitch, interval)
        if val != "None":
            pitches.append((interval, val))
    return pitches

def melody_interval_down(pitch: str):
    pitches = []
    for interval in melody_intervals:
        val = low_pitch_solver(pitch, interval)
        if val != "None":
            pitches.append((interval, val))
    return pitches

def melody_and_pitch(melodies, pitch: str):
    out = []
    banned = {"D4", "P4", "A4", "D5", "D7", "m7", "M7", "A7", "D2", "m2", "M2", "A2", "Error"}
    for interval, note in melodies:
        val = interval_solver(pitch, note)
        if val not in banned:
            out.append([val, interval, note])
    return out
