class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    heal_step = 10

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self, power):
        print(f"{self.name} attacks with {power}!")

    # TODO: Define heal method and implement it
    def heal(self):
        self.health += SuperHero.heal_step
        print(f"{self.name} heals {SuperHero.heal_step} points. New health: {self.health}.")
     

# TODO: Create superhero instance
superhero = SuperHero('Catwoman', 'Agility', 120)

# TODO: Use the attack() and heal() method
superhero.attack('Agility')
superhero.heal()