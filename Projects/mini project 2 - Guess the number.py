# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
secret_number = 0 
guesses_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_number
    global guesses_left

    # define event handlers for control panel

    secret_number = random.randrange(0, num_range)
 
    if num_range == 100:
        guesses_left = 7  
    elif num_range == 1000:
        guesses_left = 10 
    
    print "New game. The range is from 0 to", num_range
    print "Number of remaining guesses is ", guesses_left, "\n"
    
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()
        
def input_guess(guess):
    # main game logic goes here
    global guesses_left
    global secret_number
    
    won = False
    
    print "Guess was ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left

    if int(guess) == secret_number:
        won = True
    elif int(guess) > secret_number:
        result = "Lower!"
    else:
        result = "Higher!"

    if won:
        print "That is correct!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in due time!"
        new_game()
        return
    else:
        print result
        
# create frame
frame = simplegui.create_frame("Game: Guess the number!", 250, 250)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)
frame.add_input("Enter your guess", input_guess, 100)

# call new_game
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
