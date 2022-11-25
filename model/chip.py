from dataclasses import dataclass

@dataclass
class Chip:
    
    val : int

    def __init__(self, faceval : int) -> None:
       self.val = faceval
    

