"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
#import pandas
class Pokemon(ABC):
    """
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int):
        self._name = name
        self._level = level
        self._strenght = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
    """
    
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self.level
    @property
    def strength(self):
        return self._strength 
    @property
    def defense(self):
        return self._defense
