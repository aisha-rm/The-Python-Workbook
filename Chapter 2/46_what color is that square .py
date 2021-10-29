"""
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row.

Write a program that reads a position from the user. Use an if statement to
determine if the column begins with a black square or a white square. Then use
modular arithmetic to report the color of the square in that row. For example, if the
user enters a1 then your program should report that the square is black. If the user
enters d5 then your program should report that the square is white. Your program
may assume that a valid position will always be entered. It does not need to perform
any error checking.
"""

position = input("Please enter a position on the chess board: ")

col = position[0]        #column from user
row = int(position[1])  #row from users

white_column = ["b", "d", "f", "h"]
black_column = ["a", "c", "e", "g"]

if col in white_column:
    print("The column begins with a white square.")
elif col in black_column:
    print("The column begins with a black square.")
    
        
