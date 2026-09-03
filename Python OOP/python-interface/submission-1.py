from abc import ABC, abstractmethod
from typing import override, final

# TODO: Create a Superhero interface
class Superhero(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass
    
    @abstractmethod
    def use_power(self) -> str:
        pass

@final
class Superman(Superhero):

    @override
    def fly(self) -> str:
        return "Up, up and away!"
    
    @override
    def use_power(self) -> str:
        return "Using heat vision"

class WonderWoman(Superhero):
    def fly(self) -> str:
        return "Soaring through the clouds!"
    
    def use_power(self) -> str:
        return "Using lasso of truth"



# Don't modify the code below
superman = Superman()
wonder_woman = WonderWoman()

print(isinstance(superman, Superhero)) 
print(isinstance(wonder_woman, Superhero))
