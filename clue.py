#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:53:24 2018

@author: Pritesh Patel

"""

#import my other modules, one is a set of helper definitions and functions and
#the other is a module with all the class definitions

from clue_helpers import *
from clue_classes import *
          

"""
MAIN 

This is the main control of the Clue Game Program. It initializes the
game and then runs a loop for the user to take turns. To break out of 
the loop the user can exit the game or correctly guess the answer
"""

#Display intro screen and messages

display_intro()

#Ask user to pick a character
print("\nPlease pick one of these 6 characters to represent you:")
user = validate_input(guests)

#Ask user to pick a number of players to play with
possible_num_players = [1,2,3,4,5]
print("\nHow many CPU players would you like to play against (choose 1 - 5)?")
num_cpu_players = validate_input(possible_num_players)

#initialize the game with user picked character and total number of players
g1=Game(user, num_cpu_players+1)
g1.start_game()

#track if the game should be ended or keep looping on turns
end_game = False

while end_game != True:
    if (g1.take_turn(user)) == True:
        end_game = True


print("\n\nThank you for playing Clue!\n\n")

