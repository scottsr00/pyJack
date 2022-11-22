import pytest

from ..model.card import Card
from ..model.deck import Deck
from ..model.hand import Hand

@pytest.fixture
def get_pairOfeights(get_deck):
    deck = get_deck
    cards = []
    for card in deck.cards:
        if (card.name == '8' and len(cards)< 2):
            cards.append(card)
    return cards


@pytest.fixture
def get_deck():
    return Deck() 

def test_hand(get_deck):
    h = Hand()
    deck = get_deck
    c1 = deck.GetCard()
    c2 = deck.GetCard()
    h.Add(c1)
    h.Add(c2)
    
    # Test split
    if len(h.cards) == 2 and (h.cards[0].name == h.cards[1].name):
        assert h.canSplit == True
    else:
        assert h.canSplit == False
    
    # hand total
    assert h.total == c1.val + c2.val

    # Test blackjack
    if h.total == 21:
        assert h.blackjack == True
    else:
        assert h.blackjack == False

def test_deck(get_deck):
    deck : Deck
    deck = get_deck
    clubs = 0
    assert deck.Count() == 52
    # test card decrement
    card = deck.GetCard()
    assert deck.Count() == 51

def test_split(get_pairOfeights):
    h = Hand()
    pair = get_pairOfeights
    assert pair[0].name == '8'
    assert pair[1].name == '8'
    assert len(pair) == 2
    for card in pair:
        h.Add(card)
    assert h.canSplit
