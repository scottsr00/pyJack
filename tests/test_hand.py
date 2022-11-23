import pytest

from ..model.card import Card
from ..model.deck import Deck
from ..model.hand import Hand

@pytest.fixture
def get_blackjack(get_deck):
    deck = get_deck
    haveAce, haveTen = False, False
    cards = []
    for card in deck.cards:
        if card.val == 1 and not haveAce:
            cards.append(card)
            haveAce = True
        if card.val == 10 and not haveTen:
            cards.append(card)
            haveTen = True
    assert len(cards) == 2
    assert cards[0].val in [1,10]
    assert cards[1].val in [1,10]
    assert cards[0].val != cards[1].val
    return cards

@pytest.fixture
def get_pairOfeights(get_deck):
    deck = get_deck
    cards = []
    for card in deck.cards:
        if (card.name == '8' and len(cards)< 2):
            cards.append(card)
    assert len(cards) == 2
    assert cards[0].val == 8
    assert cards[1].val == 8
    return cards

@pytest.fixture
def get_ace(get_deck):
    deck = get_deck
    for card in deck.cards:
        if card.name == 'Ace':
            return card

@pytest.fixture
def get_deck():
    return Deck()

def test_total(get_deck):
    h = Hand()
    deck = get_deck
    c1 = deck.GetCard()
    c2 = deck.GetCard()
    h.Add(c1)
    h.Add(c2)
    
    # hand total
    assert h.total == c1.val + c2.val

def test_blackjack(get_blackjack):
    h = Hand()
    for card in get_blackjack:
        h.Add(card)
    assert h.blackjack

def test_ace(get_ace):
    h = Hand()
    h.Add(get_ace)
    assert h.hasAce

def test_split(get_pairOfeights):
    h = Hand()
    pair = get_pairOfeights
    assert pair[0].name == '8'
    assert pair[1].name == '8'
    assert len(pair) == 2
    for card in pair:
        h.Add(card)
    assert h.canSplit
