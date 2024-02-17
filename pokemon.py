"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
#import pandas
class Pokemon(ABC):
    
    @abstractmethod
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        self._name = name
        self._level = level
        self._strenght = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
            
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value: int):
        # Setter for the level
        if isinstance(value, int) and (value>=0 and value<=100):
            self._level = value
        else:
            raise ValueError("Level must be an interger between 0 and 100")
            
    @property
    def strength(self):
        return self._strength 
    @strength.setter
    def strength(self, value: int):
        # Setter for strength
        if isinstance(value, int):
            self._strength = value
        else:
            raise ValueError("Strength must be an interger")
            
    @property
    def defense(self):
        return self._defense
    @defense.setter
    def defense(self, value: int):
        # Setter for defense
        if isinstance(value, int):
            self._defense = value
        else:
            raise ValueError("Defense must be an interger")
            
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value: int):
        # Setter for the health points
        if isinstance(value, int):
            self._hp = value
        else:
            raise ValueError("Health points must be an interger")
            
    @property
    def total_hp(self):
        return self._total_hp
    @total_hp.setter
    def total_hp(self, value: int):
        # Setter for the total health points
        if isinstance(value, int):
            self._total_hp = value
        else:
            raise ValueError("Total health points must be an interger")
            
    @property
    def agility(self):
        return self._agility
    @agility.setter
    def agility(self, value: int):
        # Setter for the agility
        if isinstance(value, int):
            self._agility = value
        else:
            raise ValueError("Agility must be an interger")
            
    @property
    def pokemon_type(self):
        return self._pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, value: str):
        # Setter for the pokemon type
        if isinstance(value, str):
            self._pokemon_type = value
        else:
            raise ValueError("Pokemon type must be a string")

    @abstractmethod 
    def effectiveness(self, opponent: 'Pokemon') -> int: 
        pass
    
    def basic_attack(self, opponent: 'Pokemon') -> int:
        difference = self._strength - opponent._defense 
        damage = max(1,difference)
        opponent._hp -= damage
        return damage
    
    def is_debilitated(self) -> bool: 
        return self._hp == 0
    
    def  __str__(self) -> str:
        string = f"{self._name} ({self._pokemon_type}) Stats: Level: {self._level}, ATT: {self._strength}, DEF: {self._defense}, AGI: {self._agility}, HP: {self._hp}/{self._total_hp}"
        return string
