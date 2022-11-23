import pytest

from ..model.deck import Deck
from ..model.card import Card

@pytest.fixture
def get_deck():
    return Deck() 

def test_deck(get_deck):
    deck : Deck
    deck = get_deck
    clubs = 0
    assert deck.Count() == 52
    # test card decrement
    card = deck.GetCard()
    assert deck.Count() == 51