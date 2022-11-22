from dataclasses import dataclass
from typing import List
from .card import Card

@dataclass
class Hand():
    """ Handles all hand related attributes, including cards and properties of the game"""
    cards : List[Card] 
    total : int 
    display : str
    hasAce: bool
    hasAceOption: bool
    isDealer : bool
    bust : bool
    blackjack : bool
    canSplit : bool
    
    # remove a card from the current hand - we'll create another hand with the same
    def Split(self):
        return(Hand(self.cards.pop()))

    def Cards(self) -> List[Card]:
        return self.cards

    def Add(self, card):
        self.cards.append(card)
        self.total = 0
        self.hasAceOption = False
        for c in self.cards:
            self.total += c.val
            if c.val == 1:
                self.hasAce = True
        if self.hasAce and self.total+10 <=21:
                self.hasAceOption = True
                self.total+=10
        if self.total > 21:
            self.bust = True
        if self.total == 21:
            self.blackjack = True
        if len(self.cards) == 2 and (self.cards[0].name == self.cards[1].name):
            self.canSplit = True
        else:
            self.canSplit = False


    def __init__(self, card:Card=None, isDealer=False) -> None: 
        self.total = 0
        self.display = ''
        self.hasAce = False
        self.hasAceOption = False
        self.isDealer = isDealer
        self.bust = False
        self.blackjack = False
        self.cards = []
        self.canSplit = False
        if not card is None:
            self.Add(card)
        

    def __str__(self) -> str:
        self.display = ''
        for card in self.cards:
            self.display += (f'{card}')
        return(self.display)
    
    def Summary(self):
        summary : str  = 'You have'
        if self.isDealer:
            summary = 'Dealer has'
        if self.hasAceOption:
            summary += f': {self.total-10}/{self.total}\n\n'
        else:
            summary += f': {self.total}\n\n'
        summary += f'{self}'
        if self.blackjack:
            summary += '\n\nBlackjack!!!'
        if self.bust:
            summary += '\n\nBust!!'

        return summary