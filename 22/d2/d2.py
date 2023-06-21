"""With this puzzle, the first thing that came to mind were dictionaries since they reduce amount
of conditionals and clustermess. The plan worked but I had to use one too many because of the problems
caused by using for loops and conditionals together, and I was thus forced to use three for loops with
an if statement, albeit it did look neater. So, the code is a bit longer than needed. It also had way
too many errors and took longer than it should've for correction."""

# Dictionaries initialization.
shape_points = {'X': 1,'Y': 2, 'Z': 3}
winning_combo = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
losing_combo = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
drawing_combo = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

# Lists and file initialized.
filename = 'd2.txt'
opponent_play = []
user_play = []

# Two with blocks, first to seperate my and my opponent's moves into different lists and
# then needed to use the second to check the length of the file. (I did not want to just count the
# lines myself, nor is it possible to do two read statements in one with block)
with open(filename, 'r') as f:
    file = f.read()
    
    for char in file:
        
        if char == 'A' or char == 'B' or char == 'C':
            opponent_play.append(char)

        elif char == 'X' or char == 'Y' or char == 'Z':
            user_play.append(char)
        
        else:
            pass

with open(filename, 'r') as f:
    file_length = len(f.readlines())

# Variable initialization for main while loop.
n = 0
score = 0
total_score = 0

while True:
    # Made lists variables, used conditionals and for loops to get score of player and found total
    # score at the end. Used basic totalling to continue the while loop. 

    play = opponent_play[n]
    response = user_play[n]
    
    for key, value1 in winning_combo.items():

        if play == key and response == value1:

            score = shape_points[response] + 6

    for key, value2 in losing_combo.items():

        if play == key and response == value2:

            score = shape_points[response]
                
    for key, value3 in drawing_combo.items():
        
        if play == key and response == value3:
            
            score = shape_points[response] + 3
    
    total_score += score
    n += 1

    if n >= file_length:
        break

print(f"The total score attained by following the strategy guide is {total_score} points.")