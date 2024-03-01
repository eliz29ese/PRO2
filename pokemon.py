"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
#import pandas
class Pokemon(ABC):
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
        
        

    def  __str__(self) -> str:
        string = f"{self._name} ({self._pokemon_type}) Stats: Level: {self._level}, ATT: {self._strength}, DEF: {self._defense}, AGI: {self._agility}, HP: {self._hp}/{self._total_hp}"
        return string
    
    
    @property
    def name(self):
        return self.name
   
            
    @property
    def level(self):
        return self.level
    @level.setter
    def level(self, value: int):
        # Setter for the level
        if isinstance(value, int) and (value>=0 and value<=100):
            self.level = value
        else:
            raise ValueError("Level must be an interger between 0 and 100")
            
    @property
    def strength(self):
        return self._strength 
    @strength.setter
    def strength(self, value: int):
        # Setter for strength
        if isinstance(value, int):
            self.strength = value
        else:
            raise ValueError("Strength must be an interger")
            
    @property
    def defense(self):
        return self.defense
    @defense.setter
    def defense(self, value: int):
        # Setter for defense
        if isinstance(value, int):
            self.defense = value
        else:
            raise ValueError("Defense must be an interger")
            
    @property
    def hp(self):
        return self.hp
    @hp.setter
    def hp(self, value: int):
        # Setter for the health points
        if isinstance(value, int):
            self.hp = value
        else:
            raise ValueError("Health points must be an interger")
            
    @property
    def total_hp(self):
        return self.total_hp
    
            
    @property
    def agility(self):
        return self.agility
    @agility.setter
    def agility(self, value: int):
        # Setter for the agility
        if isinstance(value, int):
            self.agility = value
        else:
            raise ValueError("Agility must be an interger")
            
    @property
    def pokemon_type(self):
        return self.pokemon_type
        
    @pokemon_type.setter
    def pokemon_type(self, value: str):
        # Setter for the pokemon type
        if isinstance(value, str):
            self.pokemon_type = value
        else:
            raise ValueError("Pokemon type must be a string")

    @abstractmethod 
    def effectiveness(self, opponent: 'Pokemon') -> int: 
        pass
    
    def basic_attack(self, opponent: 'Pokemon') -> int:
        damage = max(1, self.strength - opponent.defense )
        opponent.hp -= damage
        opponent.hp = max(0, opponent._hp)
        return damage
    
    def is_debilitated(self) -> bool: 
        return self.hp == 0
    
   


class WaterPokemon(Pokemon):
    
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, surge_mode:bool = False):
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Water") 
        self._surge_mode = surge_mode
        
    @property
    def surge_mode(self):
        return self.surge_mode
    
    @surge_mode.setter
    def surge_mode(self, value: bool):
        # Setter for the surge mode
        if isinstance(value, bool):
            self.surge_mode = value
        else:
            raise ValueError("Pokemon type must be a boolean")

    def check_surge_activation(self)->bool:
        return self.hp < (self.total_hp/2)
        
    def water_attack(self, p: Pokemon) -> int:
        if self.check_surge_activation():
            self.surge_mode = True
        else:
            self.surge_mode = False
            
        factor = 1 if p.pokemon_type == "Water" else (0.5 if p.pokemon_type == "Grass" else 1.5)
            
        if self._surge_mode == True:
            factor += 0.1
            
        water_damage = int(max(1, (factor*self.strength - p.defense)))
        p.hp -= water_damage  
        p.hp = max(0, p.hp)
        return water_damage
    
    def effectiveness(self, p: Pokemon) -> int:
        return (-1 if p.pokemon_type == "Grass" else (1 if p.pokemon_type == "Fire" else 0))

class GrassPokemon(Pokemon):
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, healing:float):
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Grass")
        self._healing = healing
        
    @property
    def healing(self):
            return self.healing
    @healing.setter
    def healing(self, value: float):
            # Setter for the temperature
            if isinstance(value, float):
                self.healing = value
            else:
                raise ValueError("Healing must be a float")
                
    def grass_attack(self, p: Pokemon) -> int:
        factor = 1.5 if p.pokemon_type == "Water" else (1 if p.pokemon_type == "Grass" else 0.5)
        grass_damage = int((max(1, (factor*self.strength) - p.defense))) 
        p.hp -= grass_damage
        p.hp = max(0, p.hp)
            
        return grass_damage 
        
    def heal(self) -> int:
        n = int(self.healing*self.hp)
        self.hp += n
        if self.hp > self.total_hp:
            self.hp = self.totalhp
        return n
    
    def effectiveness(self, p: Pokemon) -> int:
        return (0 if p.pokemon_type == "Grass" else (-1 if p.pokemon_type == "Fire" else 1))
            
class FirePokemon(Pokemon):
        
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, temperature:float):
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Fire")
        self._temperature = temperature
        
    @property
    def temperature(self):
            return self.temperature
    @temperature.setter
    def temperature(self, value: float):
            # Setter for the temperature
            if isinstance(value, float):
                self.temperature = value
            else:
                raise ValueError("Temperature must be a float")
                
    def fire_attack(self, p:Pokemon)-> int:
            factor = 1.5 if p.pokemon_type == "Grass" else (1 if p.pokemon_type == "Fire" else 0.5)
            fire_damage = int((max(1, (factor*self.strength) - p.defense)))
            p.hp -= fire_damage
            p.hp = max(0, p.hp)
                
            return fire_damage 
        
    def embers(self, p: Pokemon) -> int: 
            embers_damage = int((self.strength*self.temperature))  
            p.hp -= embers_damage
            p.hp = max(0, p.hp)  
            return embers_damage
        
    def effectiveness(self, p: Pokemon) -> int:
            return (1 if p.pokemon_type == "Grass" else (0 if p.pokemon_type == "Fire" else -1))
            
