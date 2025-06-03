# Traditional Music Composer Assistant

A sophisticated C++ tool that assists in traditional music composition by suggesting valid melodic progressions based on musical theory rules and interval relationships.

## Features

- **Melodic Suggestion Engine**: Suggests possible next notes in a melody based on:
  - Previous note
  - Desired direction (ascending or descending)
  - Valid musical intervals
  - Harmonic compatibility

- **Comprehensive Musical Theory Implementation**:
  - Full piano keyboard layout support
  - Complete interval system including:
    - Perfect intervals (P1, P4, P5, P8)
    - Major intervals (M2, M3, M6, M7)
    - Minor intervals (m2, m3, m6, m7)
    - Augmented intervals (A1, A2, A3, A4, A5, A6, A7)
    - Diminished intervals (D2, D3, D4, D5, D6, D7, D8)
  - Intelligent filtering of dissonant intervals

- **Smart Musical Analysis**:
  - Calculates intervals between any two notes
  - Determines valid next pitches based on interval constraints
  - Handles enharmonic equivalents (e.g., C# = Db)
  - Supports octave transformations

## Usage

1. Run the program
2. Input the previous melody note (e.g., "mC" for middle C, "#F" for F-sharp)
3. Input the reference pitch
4. Choose direction:
   - Enter "U" for ascending suggestions
   - Enter "D" for descending suggestions
5. View the suggested next notes, with their intervals and relationships

### Note Format
- Use prefix notation for accidentals:
  - "#" for sharp (e.g., "#F" for F-sharp)
  - "b" for flat (e.g., "bB" for B-flat)
  - "m" for natural (e.g., "mC" for natural C)

### Example Output
```
Previous melody: mC
Pitch: mG
Up or Down: U
P5 : P1 = mG
m6 : m2 = mA
M6 : M2 = #A
```
Each line shows: `[Interval with reference pitch] : [Melodic interval] = [Suggested next note]`

## Technical Details

The program uses several sophisticated algorithms to:
- Calculate keyboard distances between notes
- Determine valid intervals based on note positions
- Filter out dissonant or theoretically incorrect progressions
- Handle edge cases like octave wrapping

## Requirements

- C++ compiler with C++11 support or later
- Standard Template Library (STL)

## Running the Program

### Pre-compiled Executables for Apple Silicon Macs
If you're using a Mac with Apple Silicon (M1/M2/M3), you can use the pre-compiled executables in the `MacOS_ARM` directory:

#### Main Composer Program
```bash
# Navigate to the MacOS_ARM directory
cd MacOS_ARM/

# Run the composer program
./composer
```

#### Additional Tools
The MacOS_ARM directory also includes specialized tools:

- **interval_solver**: Calculates the interval between two given notes
  ```bash
  ./interval_solver
  ```

- **pitch_solver**: Finds possible notes at a given interval from a reference note
  ```bash
  ./pitch_solver
  ```

### Building from Source
If you need to build the program from source:
```bash
# Navigate to the source code directory
cd source_code/

# Compile the program
g++ -std=c++11 composer.cpp -o composer
```

### Using the Program
1. After building, run the program:
   ```bash
   ./composer
   ```
2. The program will prompt you for input in the following order:
   - Enter your previous melody note (e.g., "mC" for middle C)
   - Enter the reference pitch (e.g., "mG" for G)
   - Choose direction ("U" for up or "D" for down)

3. The program will display possible next notes, showing:
   - The interval relationship with the reference pitch
   - The melodic interval from the previous note
   - The suggested next note

4. The program runs continuously, allowing you to explore multiple melodic possibilities. Press Ctrl+C (Command+C on Mac) to exit.

## Python GUI Composer

If you prefer a simple graphical interface that automatically generates random melodies, run the `auto_song_gui.py` script:

```bash
python3 auto_song_gui.py
```

This GUI lets you choose the number of notes to generate and provides basic playback using `pygame`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
