from dataclasses import dataclass
from .chip import Chip
import pdb

@dataclass
class Chipstack:    

    chipstack = []
    
    def Create(self, no, val):
        for i in range(no):
            chip = Chip(val)
            self.chipstack.append(chip)

    def GetCount(self) -> int:
        return len(self.chipstack)
 
    def GetTotal(self) -> int:
        total = 0
        for chip in self.chipstack:
            total += chip.val
        return total

    def Add(self, chips):                  
        for chip in chips:
            self.chipstack.append(chip)

    def clean(self):
        cleanstack = []
        for chip in self.chipstack:
            if chip.val > 0:
                cleanstack.append(chip)
            else:
                print("Chip with value 0 or less found and discarded")
        self.chipstack = cleanstack



    def Remove(self, amountToRemove) -> int:
        removed = 0
    
        for chip in self.chipstack:
            if removed < amountToRemove:
                if chip.val <= (amountToRemove - removed):
                    removed += chip.val
                    chip.val = 0
            else:
                break
        self.clean()      
        return removed
    
    