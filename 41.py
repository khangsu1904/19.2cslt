note_freq = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

note = input("Nhap mot not tu C0 den C8: ")
letter = note[0]
octave = int(note[1])

if letter in note_freq:
    freq = note_freq[letter] * (2 ** (4- octave))
    print(f"Tan so cua {note} la {freq} Hz")
else:
    print("Not khong hop le!")
