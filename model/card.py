from dataclasses import dataclass

@dataclass
class Card:
    rank : int
    val : int
    suit : str
    name : str

    def __str__(self) -> str:
        return(f'{self.name}-{self.suit}\n')