"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
#import pandas
class Pokemon(ABC):
    """
    A class of Pokemon objects, elements used in battles to fight against each other.
    
    Attributes
    ----------
    name : str
        Name of the Pokemon.
    level : int
        Level of the Pokemon.
    strength : int
        Strength of the Pokemon.
    defense : int
        Defense of the Pokemon.
    hp : int
        Current health points of the Pokemon.
    total_hp : int
        Maximum health points of the Pokemon.
    agility : int
        Agility of the Pokemon.
    pokemon_type : str
        Type of the Pokemon.
    
    Methods
    -------
    __str__() -> str:
        Returns a string with the Pokemon's properties.
    effectiveness(opponent: 'Pokemon') -> int:
        Abstract method used to determine the effectiveness of a Pokemon against its opponent,
        to be implemented by subclasses.
    basic_attack(opponent: 'Pokemon') -> int:
        Carries out a basic attack on the opponent and calculates the damage done. It also updates
        the opponent's health points.
    is_debilitated() -> bool:
        Checks that the Pokemon is not debilitated, that its HP is not 0. Returns True if debilitated,
        if not False.
    """

      
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        """
        Creates a Pokemon object with the attributes given.
     
        Parameters
        ----------
        name : str
            Name of the Pokemon.
        level : int
            Level of the Pokemon.
        strength : int
            Strength attribute of the Pokemon.
        defense : int
            Defense attribute of the Pokemon.
        hp : int
            Current health points of the Pokemon.
        total_hp : int
            Maximum health points of the Pokemon.
        agility : int
            Agility attribute of the Pokemon.
        pokemon_type : str
            Type of the Pokemon.
     
        Returns
        -------
        None
        """
        
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
        
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
        

    def  __str__(self) -> str:
        """
        Returns a string with the Pokemon's properties.
    
        Returns
        -------
        str
            String containing the Pokemon's properties.
        """
        string = f"{self._name} ({self._pokemon_type}) Stats: Level: {self._level}, ATT: {self._strength}, DEF: {self._defense}, AGI: {self._agility}, HP: {self._hp}/{self._total_hp}"
        return string
    
    
    @property
    def name(self):
        return self._name
   
            
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
        """
        Abstract method used to determine the effectiveness of a Pokemon against its opponent,
        to be implemented by subclasses.
    
       Parameters
       ----------
       opponent : Pokemon
           The opponent Pokemon.
    
       Returns
       -------
       int
           The effectiveness of the attack aggainst the opponent.
       """
        pass
    
    def basic_attack(self, opponent: 'Pokemon') -> int:
        """
        Carries out a basic attack on the opponent and calculates the damage done. It also updates
        the opponent's health points.
        
        Parameters
        ----------
        opponent : Pokemon
            The opponent Pokemon.
        
        Returns
        -------
        int
            The damage done to the opponent.
        """
        damage = max(1, self.strength - opponent.defense )
        opponent.hp -= damage
        opponent.hp = max(0, opponent._hp)
        return damage
    
    def is_debilitated(self) -> bool: 
        """
        Checks that the Pokemon is not debilitated, that its HP is not 0. 
        
        Returns
        -------
        bool
            True if the Pokemon is debilitated, if not False.
        """
        return self.hp == 0
    
   


class WaterPokemon(Pokemon):
    """
    A subclass of Pokemon with the Water type.
    
    Attributes
    ---------- 
    surge_mode : bool 
        A boolean attribute that represents the surge mode of a Water Pokemon.

    Methods 
    ------- 
    check_surge_activation() -> bool:
        Checks if the Pokemon's HP attribute is less than half of its total_hp, returning True if so.

    water_attack(p: Pokemon) -> int:
        Executes a water attack, calculating the damage dealt as an interfer of the maximum 
        between 1 and  (factor*strength - defense), obtaining the value factor beforehand based on
        the opponent's class. If the surge_mode attribute is True, the factor increases
        by 0.1. Returns the damage done.

    effectiveness(p: Pokemon) -> int:
        Establishes the effectiveness of the Water Pokemon based on the class of its opponent.
    """

    
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, surge_mode:bool = False):
        """
        Creates a Water Pokemon object with the given attributes, inheriting attributes
        from the Pokemon class.
     
        Parameters
        ----------
        surge_mode : bool 
            A boolean attribute that represents the surge mode of a Water Pokemon
     
        Returns
        -------
        None
        
        """
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Water") 
        self._surge_mode = surge_mode
        
    @property
    def surge_mode(self):
        return self._surge_mode
    
    @surge_mode.setter
    def surge_mode(self, value: bool):
        # Setter for the surge mode
        if isinstance(value, bool):
            self._surge_mode = value
        else:
            raise ValueError("Pokemon type must be a boolean")

    def check_surge_activation(self)->bool:
        """
        Checks if the Pokemon's HP attribute is less than half of its total_hp, returning True if so.
        
        Returns
        -------
        bool
            True si el valor de HP es inferior que la mitad de su total_hp.
        """
        return self.hp < (self.total_hp/2)
        
    def water_attack(self, p: Pokemon) -> int:
        """
        Executes a water attack, calculating the damage dealt as an interfer of the maximum 
        between 1 and  (factor*strength - defense), obtaining the value factor beforehand based on
        the opponent's class. If the surge_mode attribute is True, the factor increases
        by 0.1.
        
        Returns
        -------
        int
            Returns the damage caused to the opponent.
        """
        if self.check_surge_activation():
            self._surge_mode = True
        else:
            self._surge_mode = False
            
        factor = 1 if p.pokemon_type == "Water" else (0.5 if p.pokemon_type == "Grass" else 1.5)
            
        if self._surge_mode == True:
            factor += 0.1
            
        water_damage = int(max(1, (factor*self.strength - p.defense)))
        p.hp -= water_damage  
        p.hp = max(0, p.hp)
        return water_damage
    
    def effectiveness(self, p: Pokemon) -> int:
        """
        Establishes the effectiveness of the Water Pokemon based on the class of its 
        opponent.        
        Returns
        -------
        int
            The effectiveness value: -1 if the opponent type is Grass, 1 if is Fire and
            0 if is Water.
        """
        return (-1 if p.pokemon_type == "Grass" else (1 if p.pokemon_type == "Fire" else 0))

class GrassPokemon(Pokemon):
    """
    A subclass of Pokemon with the Grass type.
    
    Attributes
    ---------- 
    healing : float 
        Attribute used to increase the health points of the Pokemon after performing a
        specific class attack (grass_attack).

    Methods 
    ------- 
    grass_attack(p: Pokemon) -> int:
        Executes a grass attack, calculating the damage dealt as an interference of the maximum 
        between 1 and (factor*strength - defense), obtaining the factor value beforehand based on
        the opponent's class. Returns the damage done.
        
    heal() -> int:
        Heals the Pokemon by n units, the integer part of healing*hp, returning n. Increases the value
        of hp by n units.
            
    effectiveness(p: Pokemon) -> int:
        Establishes the effectiveness of the Grass Pokemon based on the class of its opponent.
    """
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, healing:float):
        """
        Creates a Grass Pokemon object with the given attributes, inheriting attributes
        from the Pokemon class.
     
        Parameters
        ----------
        healing : float 
            Attribute used to increase the health points of the Pokemon after performing a
            specific class attack (grass_attack).
     
        Returns
        -------
        None
        
        """
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Grass")
        self._healing = healing
        
    @property
    def healing(self):
            return self._healing
    @healing.setter
    def healing(self, value: float):
            # Setter for the temperature
            if isinstance(value, float):
                self._healing = value
            else:
                raise ValueError("Healing must be a float")
                
    def grass_attack(self, p: Pokemon) -> int:
        """
        Executes a grass attack, calculating the damage dealt as an interference of the maximum 
        between 1 and (factor*strength - defense), obtaining the factor value beforehand based on
        the opponent's class.
        
        Returns
        -------
        int
            Returns the damage caused to the opponent.
        """
        factor = 1.5 if p.pokemon_type == "Water" else (1 if p.pokemon_type == "Grass" else 0.5)
        grass_damage = int((max(1, (factor*self.strength) - p.defense))) 
        p.hp -= grass_damage
        p.hp = max(0, p.hp)
            
        return grass_damage 
        
    def heal(self) -> int:
        """
        Heals the Pokemon by n units, the integer part of healing*hp. Increases the value
        of hp by n units.
        Returns
        -------
        int
            The healing points added.
        """
        n = int(self.healing*self.hp)
        self.hp += n
        if self.hp > self.total_hp:
            self.hp = self.total_hp
        return n
    
    def effectiveness(self, p: Pokemon) -> int:
        """
        Establishes the effectiveness of the Grass Pokemon based on the class of its 
        opponent.        
        Returns
        -------
        int
            The effectiveness value: 0 if the opponent type is Grass, -1 if is Fire and
            1 if is Water.
        """
        return (0 if p.pokemon_type == "Grass" else (-1 if p.pokemon_type == "Fire" else 1))
            
class FirePokemon(Pokemon):
        
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, temperature:float):
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Fire")
        self._temperature = temperature
        
    @property
    def temperature(self):
            return self._temperature
    @temperature.setter
    def temperature(self, value: float):
            # Setter for the temperature
            if isinstance(value, float):
                self._temperature = value
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
            
