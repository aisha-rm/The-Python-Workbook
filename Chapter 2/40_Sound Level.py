"""
The following table lists the sound level in decibels for several common noises.
    Noise       Decibel Level
    Jackhammer      130 dB
    Gas Lawnmower   106 dB
    Alarm Clock     70 dB
    Quiet Room      40 dB
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

noise = {"Jackhammer":130, "Gas Lawnmover":106, "Alarm Clock":70, "Quiet Room":40}
sounds = [("Jackhammer", 130), ("Gas Lawnmover", 106), ("Alarm Clock", 70), ("Quiet Room", 40)]
lst = []

for key, value in noise.items():
    
    if not value in lst:
        lst.append(value)
        
decibel = int(input("Enter the number of decibels: "))

if decibel < min(lst):
    print("This is quieter than a Quiet Room")
elif decibel > max(lst):
    print("This is louder than a Jackhammer")
else:
    # for key, value in sounds.items():
    #     if decibel == value:
    #         print(f"This is equivalent to the sound of a/an {key}")
    for i in range(len(sounds)):
        if decibel == sounds[i][1]:
            print(f"This is equivalent to the sound of a/an {sounds[i][0]}")
        elif sounds[i][1] > decibel > sounds[i+1][1]:
            print(f"This is equivalent to the sound between a/an {sounds[i][0]} and a/an {sounds[i+1][0]}") 