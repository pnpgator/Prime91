#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  27 17:36:33 2018

@author: Pritesh Patel
"""
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


guests = ["Professor Plum", "Miss Scarlet", "Reverend Green", "Mrs White", 
          "Colonel Mustard", "Madame Peacock"]

guest_short = [" Plum  ","Scarlet"," Green "," White ","Mustard","Peacock"]

weapons = ["Candlestick", "Knife", "Lead Pipe", "Revolver", "Rope",
           "Wrench", "Axe", "Poison", "Bat"]

rooms = [["Library",["Hall", "Dining Room", "Garage"]],
         ["Hall",["Library", "Basement", "Study"]],         
         ["Study",["Hall", "Theater", "Kitchen"]],
         ["Dining Room", ["Library", "Basement", "Kitchen"]],
         ["Basement", ["Dining Room", "Hall", "Conservatory", "Theater"]],
         ["Theater", ["Study", "Basement", "Garage"]],
         ["Kitchen", ["Conservatory", "Dining Room", "Study"]],
         ["Conservatory", ["Kitchen", "Basement", "Garage"]],
         ["Garage", ["Conservatory", "Theater", "Library"]] ]

choices = ["Make a guess","See my cards","Move to a different room","Scratch Pad","Display Rules","Exit Game"]

def clear_screen():
    """
    Clears the terminal screen. I found this code snippet on Stack Overflow to
    use the right OS command for Windows and Mac.
    """

    command = "-cls" if system_name().lower()=="windows" else "clear"

    system_call(command)


def validate_input(possible_choices):
   """
   Validates user inputs by creating a numbered menu and making sure the user
   picks from the numbered menu. The input is a list which this function will
   assign a number to each item and then ask the user to pick a number
   corresponding to the item they would like to choose. The output returns the
   value of the choice as the list item that was chosen
   """

#list out the choices

   for idx, choice in enumerate(possible_choices):
       print (idx+1, "-", choice)

#Keep asking the user for a number that corresponds to one of the choices

   while True:
       while True:
#first try to see if the choice is really a number
           try:
               user_input = int(input("Please enter a number between 1 and {}:".format(len(possible_choices))))                                
               break
            
           except ValueError:
               print("That was not a valid number.  Try again...")

#then see if the choice is a valid number that matches the choice options

       user_choice = int(user_input)
       if (user_choice < 1 or user_choice > len(possible_choices)):
           print("\nPlease enter a number between 1 and {}.  Try again...".format(len(possible_choices)))         
       else:
           return possible_choices[user_input-1]
            
    
def display_map(locations):
    """
    This function prints out the map/board for the game. It will draw out an
    ascii text map. It takes as input a list of Location objects that show
    where each player is. The room map is hardcoded so needs to match
    the order of the rooms in the locations list that is passed in.
    """

#clear screen and init the list that tracks which room is occupied and by whom
    clear_screen()
    print_loc = []

#for each room, either create a blank space or fill in with a 7 character space
#with the name of the character/guess

    for loc in locations:

        if loc.occupant == None:
            print_loc.append("       ")
        else:
            for idx, guest in enumerate(guests):
                if guest == loc.occupant.get_name():
                    print_loc.append(guest_short[idx])
                    
#now print the map with each room populated. The room map is hardcoded so needs
#to match the order of the rooms in the locations list that is passed in.
    print("        +-------------------------------------------+")
    print("        |               |                |          |" )
    print("Garage <->   Library   <->     Hall     <-> Study  <-> Kitchen" )
    print("        |               |                |          |" )     
    print("        |   ",print_loc[0],"   |    ",print_loc[1],"   | ", print_loc[2],"|")    
    print("        |               |                |          |" )    
    print("        |      ^        |       ^        |    ^     |" )
    print("        +------|----------------|-------------|-----+")
    print("        |      v        |       v        |    v     |" )
    print("        | Dining Room  <->   Basement   <-> Theater |" )
    print("        |               |                |          |" )    
    print("        |   ",print_loc[3],"   |    ",print_loc[4],"   | ", print_loc[5],"|")
    print("        |      ^        |       ^        |    ^     |" )
    print("        +------|----------------|-------------|-----+")
    print("        |      v        |       v        |    v     |" )
    print(" Study <->   Kitchen   <-> Conservatory <-> Garage <-> Library" )  
    print("        |               |                |          |" )    
    print("        |   ",print_loc[6],"   |    ",print_loc[7],"   | ", print_loc[8],"|")
    print("        |               |                |          |" )    
    print("        +-------------------------------------------+")     
         
   
def display_intro():
    """
    This function creates a simple ASCII graphic title and then some
    intro information. It calls the display_rules function to print
    out the rules
    """

    clear_screen()
    print("       CCCCCCC   LL        UU   UU   EEEEEEE   !!!!")
    print("       CC        LL        UU   UU   EE        !!!!")
    print("       CC        LL        UU   UU   EE         !!")
    print("       CC        LL        UU   UU   EEEEE      !!")
    print("       CC        LL        UU   UU   EE         !!")
    print("       CC        LL        UU   UU   EE     ")
    print("       CCCCCCC   LLLLLLL   UUUUUUU   EEEEEEE    OO")
                
    print("\n\nWELCOME TO CLUE!\n")
    print("You are a guest at a dinner party. A murder has been committed!")
    print("Your job is to correctly guess where the murder was committed,") 
    print("using what weapon and by which guest.\n ")
    temp=input("Press Enter to Continue")
    display_rules()

    
def display_rules():   
    """
    This function prints out the rules and guidelines for the game
    """

    clear_screen()
    print("GAME RULES")
    print("------------------------------------------------------------------")
    print("\nThe murderer could be one of the 6 guests:")
    print("     ", end=" ")
    for guest in guests:
        print(guest, end=", ")
    print("\nYou will pick one of these guests to represent you, but bear in mind, that you could be the murderer\n ")
    print("The weapon could be one of these 9 weapons:")
    print("     ", end=" ")
    for weapon in weapons:
        print(weapon, end=", ")
    print("\n\nThe location of the murder could be one of these 9 rooms:")
    print("     ", end=" ")
    for room in rooms:
        print(room[0], end=", ")
    print("\nTo pick one of these rooms as part of your guess, you must be in that room at the time of your guess\n ")    
    print("To move around you can only go to certain rooms from certain rooms")
    print("The map is printed above your turn options so you can see where you can go")
    print("Whenever you make a guess, the CPU players take a turn and will move")
    print("if they can. So you should not get stuck but if you do, make some guesses!")
    print("\nThere is a card to represent each guest, room and weapon.")
    print("A guest card, a room card and a weapon card will be randomly")
    print("selected to represent the correct guess and kept aside. The")
    print("remaining cards will be dealt out to the players.")

    print("\n\nYou also have a scratch pad to keep notes, your cards and your")
    print("guesses will automatically added to your scratch pad.")


