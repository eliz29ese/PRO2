"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
#import pandas
class Pokemon(ABC):
    """
    An abstract class that enables the creation of Pokemon objects, establishing their properties 
    and basic methods, which will be complemented in its child classes to be used in battles.
    
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
        Type of the Pokemon, it will be determined by the child classes.
    
    Methods
    -------
                     ????       __str__() -> str:
                                Returns a string with the Pokemon's properties.
    effectiveness(opponent: 'Pokemon') -> int:
        Abstract method to calculate the effectiveness of a Pokemon against its opponent.
    basic_attack(opponent: 'Pokemon') -> int:
        Carries out a basic attack on the opponent, damaging its health points.
    is_debilitated() -> bool:
        Checks that the Pokemon is not debilitated.
        
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
    
    
    @property
    def name(self):
        """
        Gets the name of the Pokemon.
        
        Returns
        -------
        str
            The name of the Pokemon.
        """
        
        return self._name
   
            
    @property
    def level(self):
        """
        Gets the level of the Pokemon.
        
        Returns
        -------
        int
            The level of the Pokemon.
        """
        return self._level
    @level.setter
    def level(self, value: int):
        """
        Set the level of the Pokemon.
        
        Parameters
        ----------
        value : int
            The new level of the Pokemon.
        
        Raises
        ------
        ValueError
            If the provided value is not an integer between 0 and 100.
        """
        # Setter for the level
        if isinstance(value, int) and (value>=0 and value<=100):
            self._level = value
        else:
            raise ValueError("Level must be an integer between 0 and 100")
            
    @property
    def strength(self):
        """
        Gets the strength of the Pokemon.
        
        Returns
        -------
        int
            The strength of the Pokemon.
        """
        return self._strength 
    @strength.setter
    def strength(self, value: int):
        """
        Set the strength value of the Pokemon.
        
        Parameters
        ----------
        value : int
            The new strength value of the Pokemon.
        
        Raises
        ------
        ValueError
            If the provided value is not a positive interger.
        """
        # Setter for strength
        if isinstance(value, int) and value >= 0:
            self._strength = value
        else:
            raise ValueError("Strength must be a positive integer")
            
    @property
    def defense(self):
        """
        Gets the defense of the Pokemon.
        
        Returns
        -------
        int
            The defense of the Pokemon.
        """
        return self._defense
    @defense.setter
    def defense(self, value: int):
        """
        Set the defense attribute of the Pokemon.
        
        Parameters
        ----------
        value : int
            The new defense attribute of the Pokemon.
        
        Raises
        ------
        ValueError
            If the provided value is not a positive integer
        """
        # Setter for defense
        if isinstance(value, int) and value >= 0:
            self._defense = value
        else:
            raise ValueError("Defense must be a positive integer")
            
    @property
    def hp(self):
        """
        Gets the health points of the Pokemon.
        
        Returns
        -------
        int
            The health points of the Pokemon.
        """
        return self._hp
    @hp.setter
    def hp(self, value: int):
        """
        Set the health points of the Pokemon.
     
        Parameters
        ----------
        value : int
            The new health points for the Pokemon.
     
        Raises
        ------
        ValueError
            If the provided value is not an integer.
        """
        # Setter for the health points
        if isinstance(value, int):
            self._hp = value
        else:
            raise ValueError("Health points must be an integer")
            
    @property
    def total_hp(self):
        """
        Gets the total health points of the Pokemon.
        
        Returns
        -------
        int
            The total health points of the Pokemon.
        """
        return self._total_hp
    
            
    @property
    def agility(self):
        """
        Gets the agility of the Pokemon.
        
        Returns
        -------
        int
            The agility of the Pokemon.
        """
        return self._agility
    @agility.setter
    def agility(self, value: int):
        """
        Set the agility value of the Pokemon.
     
        Parameters
        ----------
        value : int
            The new agility value for the Pokemon.
     
        Raises
        ------
        ValueError
            If the provided value is not a positive integer.
        """
        # Setter for the agility
        if isinstance(value, int) and value>=0:
            self._agility = value
        else:
            raise ValueError("Agility must be a positive integer")
            
    @property
    def pokemon_type(self):
        """
        Gets the pokemon type of the Pokemon.
        
        Returns
        -------
        str
            The pokemon type of the Pokemon.
        """
        return self._pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, value: str):
        """
       Set the pokemon type of the Pokemon.
    
       Parameters
       ----------
       value : str
           The new pokemon type for the Pokemon.
    
       Raises
       ------
       ValueError
           If the provided value is not a non-empty string.
       """
        # Setter for the pokemon type
        if isinstance(value, str) and len(value)>0:
            self._pokemon_type = value
        else:
            raise ValueError("Pokemon type must be a non-empty string")
            
    
    def  __str__(self) -> str:
        """
        Returns a string with the Pokemon's properties.
    
        Returns
        -------
        str
            String containing the Pokemon's properties.
        """
        string = f"{self.name} ({self.pokemon_type}) Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, AGI: {self.agility}, HP: {self.hp}/{self.total_hp}"
        return string
    

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
        Carries out a basic attack on the opponent and calculates the damage done. Achieved through the strength 
        of the Pokémon, subtracting the opponent's defense value, and ensuring that the result is greater than or 
        equal to 1. It also updates the opponent's health points, subtracting the damage caused without going below 0.
        
        Parameters
        ----------
        opponent : Pokemon
            The opponent Pokemon.
        ,
        Returns
        -------
        int
            The damage done to the opponent.
        """
        damage = max(1, self.strength - opponent.defense )
        opponent.hp -= damage
        if opponent.hp < 0:
            damage += opponent.hp
            opponent.hp = 0
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

    water_attack(opponent: Pokemon) -> int:
        Executes a water attack, calculating the damage dealt and decreasing the opponent's health points.

    effectiveness(opponent: Pokemon) -> int:
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
        """
        Gets the surge mode of the Water Pokemon.
        
        Returns
        -------
        bool
            The surge mode of the Pokemon.
        """
        return self._surge_mode
    
    @surge_mode.setter
    def surge_mode(self, value: bool):
        """
       Set the surge mode of the Water Pokemon.
    
       Parameters
       ----------
       value : boll
           The new surge mode for the Pokemon.
    
       Raises
       ------
       ValueError
           If the provided value is not a boolean
       """
        # Setter for the surge mode
        if isinstance(value, bool):
            self._surge_mode = value
        else:
            raise ValueError("Pokemon type must be a boolean")
            
    def  __str__(self) -> str:
        """
        Returns a string with the Pokemon's properties.
    
        Returns
        -------
        str
            String containing the Pokemon's properties.
        """
        string = f"{self.name} ({self.pokemon_type}) Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, AGI: {self.agility}, HP: {self.hp}/{self.total_hp}, SURGE MODE: {self.surge_mode}"
        return string

    def check_surge_activation(self)->bool:
        """
        Checks if the Pokemon's HP attribute is less than half of its total_hp.
        
        Returns
        -------
        bool
            True if the HP value is lower than half of its total_hp.
        """
        return self.hp < (self.total_hp/2)
        
    def water_attack(self, opponent: Pokemon) -> int:
        """
        Executes a water attack, calculating the damage dealt as an integer of the maximum 
        between 1 and the product of the factor value and the strength of the Pokemon minus its defense, obtaining the value factor 
        beforehand based on the opponent's class. If the surge_mode attribute is True (it was activated previously with the method 
        check_surge_activation), the factor increases by 0.1. It also updates the opponent's health points, subtracting 
        the damage caused without going below 0.
        
        Returns
        -------
        int
            Returns the damage caused to the opponent.
        """
        if self.check_surge_activation():
            self._surge_mode = True
        else:
            self._surge_mode = False
            
        factor = 1 if opponent.pokemon_type == "Water" else (0.5 if opponent.pokemon_type == "Grass" else 1.5)
            
        if self._surge_mode == True:
            factor += 0.1
            
        water_damage = int(max(1, (factor*self.strength - opponent.defense)))
        opponent.hp -= water_damage  
        if opponent.hp < 0:
            water_damage += opponent.hp
            opponent.hp = 0
        return water_damage
    
    def effectiveness(self, opponent: Pokemon) -> int:
        """
        Establishes the effectiveness of the Water Pokemon based on the class of its 
        opponent.        
        Returns
        -------
        int
            The effectiveness value: -1 if the opponent type is Grass, 1 if is Fire and
            0 if is Water.
        """
        return (-1 if opponent.pokemon_type == "Grass" else (1 if opponent.pokemon_type == "Fire" else 0))

class GrassPokemon(Pokemon):
    """
    A subclass of Pokemon with the Grass type.
    
    Attributes
    ---------- 
    healing : float 
        Attribute used to increase the health points of the Pokemon after performing a
        grass attack.

    Methods 
    ------- 
    grass_attack(opponent: Pokemon) -> int:
        Executes a grass attack, calculating the damage dealt and decreasing the opponent's health points.
        
    heal() -> int:
        Heals the Pokemon, increasing the health points depending on the value of the attribute heal.
            
    effectiveness(opponent: Pokemon) -> int:
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
        """
        Gets the healing value of the Grass Pokemon.
        
        Returns
        -------
        float
            The healing value of the Pokemon.
        """
        return self._healing
    @healing.setter
    def healing(self, value: float):
        """
       Set the healing value of the Grass Pokemon.
    
       Parameters
       ----------
       value : float
           The new healing value for the Pokemon.
    
       Raises
       ------
       ValueError
           If the provided value is not a float.
       """
        # Setter for the temperature
        if isinstance(value, float):
            self._healing = value
        else:
            raise ValueError("Healing must be a float")
    def  __str__(self) -> str:
        """
        Returns a string with the Pokemon's properties.
    
        Returns
        -------
        str
            String containing the Pokemon's properties.
        """
        string = f"{self.name} ({self.pokemon_type}) Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, AGI: {self.agility}, HP: {self.hp}/{self.total_hp}, HEAL: {self.healing}"
        return string
                
    def grass_attack(self, opponent: Pokemon) -> int:
        """
        Executes a grass attack, calculating the damage dealt as an integer of the maximum 
        between 1 and the product of the factor value and the strength of the Pokemon minus its defense, 
        obtaining the factor value beforehand based on the opponent's class. It also updates the opponent's 
        health points, subtracting the damage caused without going below 0.
        
        Returns
        -------
        int
            Returns the damage caused to the opponent.
        """
        
        factor = 1.5 if opponent.pokemon_type == "Water" else (1 if opponent.pokemon_type == "Grass" else 0.5)
        grass_damage = int((max(1, (factor*self.strength) - opponent.defense))) 
        opponent.hp -= grass_damage 
        if opponent.hp < 0:
            grass_damage += opponent.hp
            opponent.hp = 0
            
        return grass_damage 
        
    def heal(self) -> int:
        """
        Heals the Pokemon, increasing the health points with the value of the product of the healing 
        attribute and its current health points. This value can never cause the current health points to 
        be greater than the total.

        Returns
        -------
        int
            The healing points added.
        """
        healing_points = int(self.healing*self.hp)
        self.hp += healing_points
        if self.hp > self.total_hp:
            healing_points -= (self.hp - self.total_hp)
            self.hp = self.total_hp
            
        return healing_points
    
    def effectiveness(self, opponent: Pokemon) -> int:
        """
        Establishes the effectiveness of the Grass Pokemon based on the class of its 
        opponent.        
        Returns
        -------
        int
            The effectiveness value: 0 if the opponent type is Grass, -1 if is Fire and
            1 if is Water.
        """
        return (0 if opponent.pokemon_type == "Grass" else (-1 if opponent.pokemon_type == "Fire" else 1))
            
class FirePokemon(Pokemon):
    """
    A subclass of Pokemon with the Fire type.
    
    Attributes
    ---------- 
    temperature : float 
        A float value representing the temperature of the Fire Pokemon, which will affect
        its ability to execute embers attack.

    Methods 
    ------- 
    fire_attack(opponent: Pokemon) -> int:
        Executes a fire attack, calculating the damage dealt and decreasing the opponent's health points.
        
    embers() -> int:
        Decreases the opponent's health points depending on the temperature attribute of the Pokemon.
            
    effectiveness(opponent: Pokemon) -> int:
        Establishes the effectiveness of the Fire Pokemon based on the class of its opponent.
    """
        
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, temperature:float):
        """
        Creates a Fire Pokemon object with the given attributes, inheriting attributes
        from the Pokemon class.
     
        Parameters
        ----------
        temperature : float 
            A float value representing the temperature of the Fire Pokemon, which will affect
            its ability to execute embers attack.
     
        Returns
        -------
        None
        
        """
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type="Fire")
        self._temperature = temperature
        
    @property
    def temperature(self):
        """
        Gets the temperature of the Fire Pokemon.
        
        Returns
        -------
        float
            The teperature of the Pokemon.
        """
        return self._temperature
    @temperature.setter
    def temperature(self, value: float):
        """
       Set the temperatue of the Fire Pokemon.
    
       Parameters
       ----------
       value : float
           The new temperature for the Pokemon.
    
       Raises
       ------
       ValueError
           If the provided value is not a float.
       """
        # Setter for the temperature
        if isinstance(value, float):
            self._temperature = value
        else:
            raise ValueError("Temperature must be a float")
                
    def  __str__(self) -> str:
        """
        Returns a string with the Pokemon's properties.
    
        Returns
        -------
        str
            String containing the Pokemon's properties.
        """
        string = f"{self.name} ({self.pokemon_type}) Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, AGI: {self.agility}, HP: {self.hp}/{self.total_hp}, TEMP: {self.temperature}"
        return string
            
    def fire_attack(self, opponent:Pokemon)-> int:
            """
            Executes a fire attack, calculating the damage dealt as an integer of the maximum 
            between 1 and the product of the factor value and the strength of the Pokemon minus its defense, 
            obtaining the factor value beforehand based on the opponent's class. It also updates the opponent's 
            health points, subtracting the damage caused without going below 0.
            
            Returns
            -------
            int
                Returns the damage caused to the opponent.
            """
            factor = 1.5 if opponent.pokemon_type == "Grass" else (1 if opponent.pokemon_type == "Fire" else 0.5)
            fire_damage = int((max(1, (factor*self.strength) - opponent.defense)))
            opponent.hp -= fire_damage  
            if opponent.hp < 0:
                fire_damage += opponent.hp
                opponent.hp = 0
                
            return fire_damage 
        
    def embers(self, opponent: Pokemon) -> int: 
            """
            Damages the opponent by decreasing its health points by the product of the strength and temperature of 
            the Pokémon, rounding down to the lower integer. It also updates the opponent's health points, subtracting 
            the damage caused without going below 0.
            
            Returns
            -------
            int
                The damage done to the opponent.
            """
        
            embers_damage = int((self.strength*self.temperature))  
            opponent.hp -= embers_damage
            if opponent.hp < 0:
                embers_damage += opponent.hp
                opponent.hp = 0
                
            return embers_damage
        
    def effectiveness(self, opponent: Pokemon) -> int:
            """
            Establishes the effectiveness of the Fire Pokemon based on the class of its 
            opponent. 
            
            Returns
            -------
            int
                The effectiveness value: 1 if the opponent type is Grass, 0 if is Fire and
                -1 if is Water.
            """
            return (1 if opponent.pokemon_type == "Grass" else (0 if opponent.pokemon_type == "Fire" else -1))
            
