#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # The program greets the user.
colors = ['red','orange','yellow','green','blue','violet','purple'] # The program initializes an array of colors.
play_again = '' # the variable play_again is set to an empty string
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #this loop continues until the user asks not to play again.
    match_color = random.choice(colors)  # a random color is selected from the seven options
    count = 0 # the number of guesses is initialized to 0
    color = '' # the input color from the user is set to an empty string
    while (color != match_color): #the game loops until the user guesses correctly.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #any spaces the user puts in the color are removed 
        count += 1 # The count storing the number of guesses increments 1
        if (color == match_color): # The program checks if the user guessed right
            print('Correct!') # and prints correct if they have
        else: # but if they haven't
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints "Sorry, try again." and your number of guesses
    
    print('\nYou guessed it in {} tries!'.format(count)) # After this victory, it prints how many tries it took the user

    if (count < best_count): # If this was the lowest number of tries they'd gotten:
        print('This was your best guess so far!') #It tells them it's a record.
        best_count = count #And sets a new record for them.

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #It asks the user if they want to play again.. (the while loop for earlier means that inputs of "no" or "n" witha ny capitalization will end the loop)

print('Thanks for playing!') # And once they're done, it thanks the user for playing.