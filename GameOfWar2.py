__author__ = 'alicia.williams'

# CIS-125 FA 2015
# Week 5: GameOfWar2.py
# File: GameOfWar2.py
# Code play the game of war similar to V1
# except when a player loses, they lose their
# card and the winning player keeps their card.
# Collaboration with Rebekah Orth and Dr. Neumann

#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print("Game is a draw")
			break
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	print("Player A has " + str(len(PlayerAHand)) + " cards.  Player B has " + str(len(PlayerBHand)) + " cards.")
	
def playRound(PlayerA, PlayerB):
	
	Acard = PlayerA.pop()
	Bcard = PlayerB.pop()
	
	rankA = getRank(Acard)
	rankB = getRank(Bcard)
	
	if rankA > rankB:
		#A wins; A gets A's card and B loses his card.
		PlayerA.insert(0,Acard)
	    
	elif rankB > rankA:
		# B wins; A loses his card and B keeps his.
		PlayerB.insert(0,Acard)
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
		
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# See the README.md file for instructions on coding 
	# This module.

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

