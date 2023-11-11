note_freq={ 'C':261.63,
            'D':293.66,
            'E':329.63,
            'F':349.23,
            'G':392.00,
            'A':440.00,
            'B':493.88}
note=input('Enter a note from C0 to C8: ')
letter=note[0]
x=int(note[1])
if letter in note_freq:
    freq=note_freq[letter]*(2**(4-x))
    print(f'Frequency of {note} is {freq}Hz')
else:
    print('Error')