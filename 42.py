f=float(input('Enter frequency:'))
a=1
if 261.63 - a <= f <= 261.63 + a:
    note = "C4"
elif 293.66 - a <= f <= 293.66 + a:
    note = "D4"
elif 329.63 - a <= f <= 329.63 + a:
    note = "E4"
elif 349.23 - a <= f <= 349.23 + a:
    note = "F4"
elif 392.00 - a <= f <= 392.00 + a:
    note = "G4"
elif 440.00 - a <= f <= 440.00 + a:
    note = "A4"
elif 493.88 - a <= f <= 493.88 + a:
    note = "B4"
else:
    note = ""
if note:
    print(f'Frequency of {note} is {f}Hz')
else:
    print('The frequency does not correspond to a known note')