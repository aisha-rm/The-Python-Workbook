"""
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.

Note Frequency (Hz)
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88

Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8. While this could be
done by adding many additional cases to your if statement, such a solution is
cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead,
you should exploit the relationship between notes in adjacent octaves. In particular,
the frequency of any note in octave n is half the frequency of the corresponding
note in octave n + 1. By using this relationship, you should be able to
add support for the additional notes without adding additional cases to your if
statement.
"""

notes = {'C4' : 261.63, 'D4' : 293.66, 'E4' : 329.63, 'F4' : 349.23, 'G4' : 392.00, 'A4' : 440.00, 'B4' : 493.88}

music_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

note = input("Please enter a note: ")
note = note.capitalize()

if (len(note) > 2) or (note[0] not in music_notes) or not(note[1].isdigit()):
    print("{} an invalid musical note. Please try again".format(note))

elif note in notes:
    print(f"The frequency of {note} is {notes[note]} Hz")
    
else:
    #separating the note into letter and octave
    letter = note[0]
    octave = int(note[1])
    for key, value in notes.items():
        if letter in key:
            freq4 = value   #frequency of letter in 4th octave
            break           #stop the loop once value is gotten
    freq_new = freq4/(2**(4-octave))    #frequency of entered letter in the octave entered
    
    print(f"The frequency of {note} is {freq_new:.2f}")