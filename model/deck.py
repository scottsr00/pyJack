import random
from dataclasses import dataclass
from typing import List
from .card import Card


SUITS = ['HEARTS', 'SPADES','DIAMONDS','CLUBS']
CARDORDER = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

@dataclass
class Deck:

    cards: List[Card]

    def GetCard(self):
        return self.cards.pop()
    
    def Shuffle(self):
        xcards = []
        while (len(self.cards) > 0):
            xcards.append(self.cards.pop(random.randint(0, len(self.cards)-1)))
        self.cards = xcards
        return xcards

    def Add(self,card):
        self.cards.append(card)

    def Count(self):
        return len(self.cards)

    def build(self):
        for index,co in enumerate(CARDORDER):
            for suit in SUITS:
                if (index+1 > 10):
                    newcard = Card(index+1, 10, suit, co)
                else:
                    newcard = Card(index+1, index+1, suit, co)
                self.Add(newcard)

    def __init__(self) -> None:
        self.cards  = []
        self.build()