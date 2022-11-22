## blackjack
## Stephen Scott Nov 6 2022
## time box: 1 day

import sys
from dataclasses import dataclass
from typing import List
from collections import OrderedDict
import time
from model.deck import Deck
from model.card import Card
from model.hand import Hand

YES = ['Y','y','Yes','YES', 'yes']
player_hands = []

def deal (hand: Hand, deck : Deck):
   
    stay = False
    hand.Add(deck.GetCard())
    if (hand.canSplit):
        print(hand.Summary())        
        print("Split, Y?")
        if (input() in YES):
            splitHand = hand.Split()
            player_hands.append(splitHand)
            deal(splitHand,deck)
     
    while not hand.bust and not hand.blackjack and not stay:
        print(hand.Summary())
        print("Hit, Y?")
        if (input() in YES):
            hand.Add(deck.GetCard())
            #print(hand.Summary())
            time.sleep(1)

        else:
            stay = True   
    print(hand.Summary())

def Play():

    #local vars
    deck = Deck()
    deck.Shuffle()

    dealer_hand = Hand(None, True)
    dealer_stay = False

    player_hand = Hand(None)  
    player_hands = []

    print('\n\n')
    print('###### ################# #######')
    print('###### ... New Round ... #######')
    print('###### ################# #######')

    # Initial Deal
    for _ in range(4):
        if (_ < 2):
            dealer_hand.Add(deck.GetCard())

    # Add the initial deal to the set of potential player hands
    player_hand.Add(deck.GetCard())
    player_hands.append(player_hand)

    # Dealer stay 17 or blackjack
    # fix this ... you can still play, only if A showing can you buy insurance
    if dealer_hand.total >=17:
        dealer_stay = True 
        if dealer_hand.blackjack:
            print(f'Dealer Backjack!\n{dealer_hand}')
            return

    print(f'\n\nDealer shows:\n\n{dealer_hand.Cards()[0]}')
   
    # start dealing player
    deal(player_hand, deck)
 
     # Final summary if staying before and further deal
     # Only after player has gone
    print(dealer_hand.Summary())

    # Dealer play
    while not dealer_hand.bust and not dealer_stay:
        print('Dealer hits....\n\n')
        time.sleep(1)
        dealer_hand.Add(deck.GetCard())
        print(dealer_hand.Summary())
        
        if dealer_hand.total >= 17:
            dealer_stay = True 

    # Final output
    if len(player_hands)> 1:
        print("multi hands")

    for pHand in player_hands:
        if (pHand.bust and dealer_hand.bust) or (dealer_hand.total == pHand.total):
            print('Push ******************')
        
        elif pHand.bust or (dealer_hand.total >= pHand.total and not dealer_hand.bust):       
            print(f'Dealer wins *************** {dealer_hand.total}, vs {player_hand.total} ***********************')
      
        else:
            print(f'Player wins *************** {pHand.total} vs {dealer_hand.total} ************************')

if __name__ == "__main__":
    
    while(True):
        time.sleep(2)
        Play()
