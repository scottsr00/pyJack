import pytest

from ..model.chip import Chip
from ..model.chipstack import Chipstack

@pytest.fixture
def create_chipStack(faceval : int = 10 , size : int = 100):
    chipstack = Chipstack()
    chipstack.Create(100, 10) 
    return chipstack

def test_ChipStack(create_chipStack):
    chipstack = create_chipStack
    assert chipstack.GetCount() == 100
    assert chipstack.GetTotal() == 1000
    assert chipstack.Remove(40) == 40
    assert chipstack.GetCount() == 96
    assert chipstack.GetTotal() == 960
    assert chipstack.Remove(100) == 100
    assert chipstack.GetCount() == 86
    assert chipstack.GetTotal() == 860
    assert chipstack.Remove(400) == 400
    assert chipstack.GetCount() == 46
    assert chipstack.GetTotal() == 460
    assert chipstack.Remove(15) == 10
    assert chipstack.GetCount() == 45
    assert chipstack.GetTotal() == 450
    assert chipstack.Remove(250) == 250
    assert chipstack.GetCount() == 20
    assert chipstack.GetTotal() == 200
     
     
