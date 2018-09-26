#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:20:19 2018

@author: Pritesh Patel
"""

#import random module for randint function, also import the clue helpers
#definitions and functions

import random
from clue_helpers import *

class Player(object):
    """
    The Player object contains attributes and methods for a player
    A player has a name, a location where they are and a set of
    player cards that was dealt to them, these attributes are initialized
    during game setup. Cards are dealt during setup using the deal_cards
    method. Location is updated using the set_location method. There is
    also a __repr__ method to display the player object as simply the players
    name.
    """
     
    def __init__(self,name, location):
        """
        Init an instance of a player object with name and location and set up
        a list for the players cards
        """
        self.name = name
        self.location = location
        self.cards = []
        
        
    def get_name(self):
        """
        Get method for player's name. Returns a string
        """
        return self.name
        
     
    def deal_card(self,card):
        """
        Deal card method to deal the player a card. The dealt card gets added to
        the players card list attribute
        """
        self.cards.append(card)
        
         
    def get_cards(self):
        """
        Get method for players cards. Returns a list of cards.
        """
        return self.cards
     
        
    def get_location(self):
        """
        Get method for players location. Returns the players location
        """
        return self.location
     
        
    def set_location(self, location):
        """
        Set method for players location. Sets the players location to whatever
        is provided by caller
        """
        self.location=location
        
       
    def __repr__(self):
        """
        Representation method for player object. Returns the string for player
        name. 
        """
        return self.name

         
class Location(object):
     """
     The Location object contains attributes and methods for a location/room
     A location has a name an occupant and a list of adjoining rooms that can
     be reached from this location. The name and adjoining locations cannot be
     changed once initialized but the occupant can change as players move around
     """
     
     def __init__(self,name, adj_locs):
         """
         Init an instance of the Location object. Each location will have a name
         and list of adjoining rooms that cannot be changed once initialized.
         The occupant can be changed as players move around
         """
         self.name = name
         self.adjoining_locations = adj_locs
         self.occupant = None
     
         
     def get_name(self):
         """
         Get method for location name. Returns a string with the name        
         """
         return self.name
     
     
     def is_occupied(self):
         """
         This method for location will return a Boolean True is the location is
         occupied and False if the room is empty.
         """
         if (self.occupant != None):
             return True
         else:
             return False
     
         
     def player_enters(self, player):
         """
         This method tracks a player entering a room. This should only be
         possible if the room is empty but we check anyway just in case.
         Then it sets the occupant attribute to the player who has been provided
         by the caller
         """
         if self.is_occupied():
             print("Error,",self.name," is already occupied by,", self.player)
         else:
             self.occupant= player
     
                     
     def player_leaves(self, player):
         """
         This method tracks a player leavint a room. This should only be
         possible if the player is in the room. We check to make sure the player
         is in the room before successfully removing the player from the
         location object
         """
         if self.occupant != player.get_name() and self.occupant != player:
             print("Error,", player,"is not in the ", self.name,". ", self.occupant," is.")
         else:
             self.occupant = None

         
     def get_adjoining_locations(self):
         """
         This method returns list of adjoining room locations that can be
         accessed from the current location
         """
         return self.adjoining_locations
     
           
     def __repr__(self):
         """
         This representation method returns a string with location name whenever
         there is a need to display the location object
         """
         return self.name     
         
     
         
class Guess(object):
    """
    The Guess class represents the elements of a guess. It includes attributes
    for a guest, weapon and room for the guess. 
    """
    
    def __init__(self,guest, weapon, room):
        """
        This method initializes the guess object which consists of a guest, room
        and weapon
        """
        self.guest = guest
        self.room = room
        self.weapon = weapon
     
         
    def __repr__(self):
        """
        This method returns a readable string to display the provided Guess
        object
        """
        return self.guest + " in the " + self.room + " with the " + self.weapon
     
   
    def __eq__(self, other):
        """
        This method allows the use of == for comparison of guesses. It compares
        all three attributes of the guess and makes suer all 3 match to consider
        the guesses as equal.
        """
        if self.guest == other.guest and self.weapon == other.weapon and self.room == other.room:
            return True
        else:
            return False
     
      
class Card(object):
    """
    This class represents a card. A card has a type called kind (guest, weapon or room)
    It also has a name that fits for that type/kind. There will be a total of 6
    guest cards, 9 weapon cards and 9 room cards 
    """
    
    def __init__(self, kind, name):
        """
        This method initializes the Card object. The card object has a kind
        (guess, weapon or room) and a name for the specific item within that
        kind
        """
        self.kind = kind
        self.name = name
     

    def get_card_kind(self):
        """
        Get method for card kind
        """
        return self.kind
     
         
    def get_card_name(self):
        """
        Get method for card name
        """
        return self.name
     
    
    def __repr__(self):
        """
        Representation method for card. Returns a string that concatenates kind
        and name 
        """
        return self.kind + ":" + self.name
         
        
class Game(object):
    """
    The Game class manages the different aspects of a Clue game. It tracks
    the players, locations, guesses and cards used in a game.
    """

    #init some basic tracking vars
    locations = []
    correct_guess = None
    scratch_pad = ""
        
    def __init__(self, user_player, num_players):
        """       
        The init method for the game class, sets up a new game. As input it
        takes the guest name that the player chooses to play with and the number
        of players the player will play against
        """       
     
        #create the location list
        for i in range (0, len(rooms)):
            current_location = Location(rooms[i][0], rooms[i][1])
            Game.locations.append(current_location)
        self.num_players = num_players
     
        #User always starts in the Garage, the last location in the list
        starting_location = Location(rooms[8][0],rooms[8][1])
        self.user_player = Player(user_player, starting_location)
        Game.locations[8].player_enters(self.user_player)
     
        #Then initialize a list of CPU players
        self.cpu_players = []
         
         
    def start_game(self):
        """       
        The start game method sets up the game by creating the CPU players
        and creating the envelope that holds the correct guess and finally
        dealing out the remaining cards to all of the players
        """       

        #initialize the CPU players
        count=1
        for idx, guest in enumerate(guests):
            if guest == self.user_player.get_name():
                continue
            else:
                current_player = Player(guest, Game.locations[idx])
                self.cpu_players.append(current_player)
                Game.locations[idx].player_enters(current_player)
                count += 1
                if count >= self.num_players:
                    break

        #Display who is who
        print("\nUser is", self.user_player)
        for count in range(0, len(self.cpu_players)):
            print("CPU Player", count+1,"is", self.cpu_players[count])
  
        #Randomly pick a correct guess                      
        envelope_guest = random.randint(0, len(guests) - 1)
        envelope_weapon = random.randint(0, len(weapons) - 1)
        envelope_room = random.randint(0, len(rooms) -1)
            
        #Create a Guess object called Correct Guess that holds the answer 
        Game.correct_guess = Guess(guests[envelope_guest], \
                              weapons[envelope_weapon], \
                              rooms[envelope_room][0])
        print("\nRandomly selected Correct Guess Cards are in the Envelope")
        
        #Create lists to hold the rest of the cards out the remaining cards
        all_cards=[[],[],[]]
        all_cards[0] = [Card("Guest", guest) for guest in guests \
                      if guest != guests[envelope_guest]] 

        all_cards[1] = [Card("Weapon", weapon) for weapon in weapons \
                      if weapon != weapons[envelope_weapon]] 

        all_cards[2] = [Card("Room", room[0]) for room in rooms \
                      if room != rooms[envelope_room]] 

        count = 0

        #Now deal out the remaining cards
        while all_cards[0] != [] or all_cards[1] != [] or all_cards[2] != []:

            #Randomly pick which kind of card to pull from. This way player gets random
            #distribution of kinds (guesses, rooms, weapons)
            which_deck = random.randint(0,2)

            #If that deck is empty then skip
            if all_cards[which_deck] == []:
                continue

            #Randomly pick which actual of card to pick. 
            which_card = random.randint(0, len(all_cards[which_deck]) - 1)

            #Distribute the cards evenly across all players
            count = count % self.num_players
            if count % self.num_players:
                self.cpu_players[count-1].deal_card(all_cards[which_deck][which_card])
            else:
                self.user_player.deal_card(all_cards[which_deck][which_card])
            count+=1
            all_cards[which_deck].pop(which_card)

        #Add the users cards automatically to the scratch pad
        Game.scratch_pad += "YOUR CARDS -" + str(self.user_player.get_cards()) + "\n"
        print("\nRemaining cards have been dealt out")
            
             
    def cpu_show_card(self, guess):
        """ 
        This method manages showing a card to the user when the user has guessed
        incorrectly. It will cycle through CPU player cards until if finds a
        card that matches the Users guess thereby proving the Guess incorrect
        It returns True when a matching card is found. It can return False if
        the card is not found which can happen when the user Guesses a card that
        they already have.
        """
             
        #go through all CPU players
        for cpu_player in self.cpu_players:
            found_card = False
            cards = cpu_player.get_cards()
             
            #go through this CPU players cards, if any of them match any part of the guess
            #show that card
            for card in cards:
                if card.name == guess.guest or card.name == guess.room or card.name == guess.weapon:
                    print("CPU Player", cpu_player," has the card: ", card)
                    Game.scratch_pad += "\nCPU Player " + str(cpu_player) +" has the card: " + str(card)
                    found_card = True
                    return True            
        else:
            print("No CPU players have the card")
            return False
      
    def make_a_guess(self):
        """ 
        This method manages the user making a guess and then evaluating that
        guess. If the guess is correct the method will return True else it will
        return False
        """ 
        print("Take a guess:")
        print("Guess Location (your current location):", self.user_player.get_location())

        #ask the user for their guess
        print("Guess the murderer")
        murderer_guess = None
        while murderer_guess not in guests:
            murderer_guess=validate_input(guests)
        print("Guess the weapon")           
        weapon_guess = None
        while weapon_guess not in weapons:
            weapon_guess=validate_input(weapons)

        #room is locked to current location for the player
        room_guess = self.user_player.get_location().get_name()

        my_guess = Guess(murderer_guess, weapon_guess,room_guess )

        #if guess is right, then print out message and return True 
        Game.scratch_pad += "\nYou guessed:" + str(my_guess)
        print("Your Guess:",my_guess)
        if my_guess == Game.correct_guess:
            print("\n***YOU GUESSED IT!***\n")
            print(Game.correct_guess)
            return True
        else:
            #else call show_card method to show who has the card that proves the guess is wrong
            print("Sorry that is not correct")
            if (self.cpu_show_card(my_guess) == False):
                for card in self.user_player.get_cards():
                    if card.name == my_guess.guest or card.name == my_guess.room or card.name == my_guess.weapon:
                        print("You have the card:", card)
                        break
                else:
                    print("ERROR - MISSING CARD") 
                
            #finally make the CPU players take a turn (move around the map/board
            self.cpu_take_turns()
        return False


    def move_rooms(self):
        """
        This method manages the user moving between rooms. It determines the
        locations the user can move to based on the connectivity provided in
        the adjoining locations list and then gives the user the option to pick
        one of those rooms to move to. It then checks that room to make sure its
        not already occupied
        """

        #get the current location of the user
        current_location = self.user_player.get_location()
            
        print("You are currently in the", current_location)
        location_options = current_location.get_adjoining_locations()
        print("From here you can go to:")
            
        #get the users choice 
        new_location = validate_input(location_options)
            
        #find the room and check if its free
        for loc in Game.locations:
            if loc.get_name() != new_location:
                continue
            else:
                if loc.is_occupied():
                    print("Sorry,",loc.occupant,"is already in that room")
                    print("If all adjoining rooms are occupied please make a")
                    print("guess which will make the CPU players will move")
                else:
            
                    #if its free, move the user from current location to their new room choice 
                    for idx, location in enumerate(Game.locations):
                        if location.get_name() == current_location.get_name():
                            Game.locations[idx].player_leaves(self.user_player)
                        else:
                            continue
                    loc.player_enters(self.user_player)
                    self.user_player.set_location(loc)
                    print("You are now in the", loc)
                break
        else:
            print("Sorry, all adjoining rooms are occupied. Please make a")
            print("guess which will make the CPU players will move")
            
    def cpu_take_turns(self):
        """
        This method manages the CPU player turns. For every CPU player, it finds
        an adjoining room that player can move to and moves them. If all
        adjoining rooms are occupied it lets the CPU player stay in place and
        prints an appropriate message about the CPU players movement.
        """
        
        print("\nCPU Players are taking turns. They will move to a new room if they can\n")
        
        for cpu_player in self.cpu_players:
            
            current_location = cpu_player.get_location()
                        
            location_options = current_location.get_adjoining_locations()
           
            for idx, loc in enumerate(Game.locations):
                if loc.get_name() not in location_options:
                    continue
                else:
                    if loc.is_occupied():
                        continue
                    else:
                        print(cpu_player, "is leaving", current_location,"and entering", loc)
                        current_location.player_leaves(cpu_player)
                        loc.player_enters(cpu_player)
                        cpu_player.set_location(loc)
                        break
                        
            else:
                print("All adjoining rooms occupied,", cpu_player,"staying in", current_location)
                       
          
    def take_turn(self,user):
        """
        This method manages the users turn. It prints out the options for the
        user and then processes their choice by calling the appropriate method
        based on their choice
        """

        #give the user a chance to continue at their pace 
        temp=input("Please press ENTER to continue")
        clear_screen()

        #display the map and then ask the user for their choice
        display_map(Game.locations)
        print("\n\nNew Turn:")
        user_turn=validate_input(choices)

        #process the user choice
        if (user_turn == "Exit Game"):
            return True
        elif (user_turn == "Scratch Pad"):
            clear_screen()
            print(Game.scratch_pad)
            more_scratch = input("Add more notes:")
            Game.scratch_pad += "\n" + more_scratch + "\n"
            print(Game.scratch_pad)
        elif (user_turn == "See my cards"):
            print("Your cards", self.user_player.get_cards())
        elif (user_turn == "Make a guess"):
            if self.make_a_guess() == True:
                return True
        elif (user_turn == "Display Rules"):
            display_rules()
        elif (user_turn == "Move to a different room"):
            self.move_rooms()
        return False  
                
