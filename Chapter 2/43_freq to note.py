"""
In the previous question you converted from a note’s name to its frequency. In this
question you will write a program that reverses that process. Begin by reading a
frequency from the user. If the frequency is within one Hertz of a value listed in
the table in the previous question then report the name of the corresponding note.
Otherwise report that the frequency does not correspond to a known note. In this
exercise you only need to consider the notes listed in the table. There is no need to
consider notes from other octaves.
"""
freq = input("Enter the frequency: ")
notes = {'C4' : 261.63, 'D4' : 293.66, 'E4' : 329.63, 'F4' : 349.23, 'G4' : 392.00, 'A4' : 440.00, 'B4' : 493.88}

if freq.replace('.','',1).isdigit(): #checking if input -which may be a decimal number- is digit
    freq = float(freq)
    for key, value in notes.items():
        if (value - 1) <= freq <= (value + 1): #checking if the frequency is within one Hertz of a value in the list
            note = key
            break                              #stop loop when note is found
        else:
            note = "none"            #if frequency not found in list of notes
        
    if note != "none":
        message = f"The corresponding note for the entered frequency {freq}Hz is {note}."   
    else:
        message = "Sorry the frequency you entered has no corresponding note. Please try again."

else:
    message = "Invalid input! Please enter numbers only."
print(message)
        