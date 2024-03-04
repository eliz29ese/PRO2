"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon

class Trainer():
    """
    A trainer is an object that represents a player in a battle, and who has multiple
    pokemons which can be used during a combat.
    
    Attributes 
    ---------- 
    name : str 
        The name of the trainer. 
    pokemon : list 
        A list that contains Pokemon objects which belong to the Trainer. 
        
    Methods 
    ------- 
    all_debilitated(self)): 
        Checks if all the pokemons of the list of the trainer are debilitated, it checks if 
        HP is zero. This function returns True if all pokemons of the trainer are debilitated.
        and False otherwise.

    select_first_pokemon(self):
        Chooses the first pokemon of the pokemon list that is not debilitated (HP is not zero).
        It returns the pokemon selected, or None if all the pokemons are debilitated.
    
    select_next_pokemon(self, p:Pokemon):
        Chooses the next pokemon in the list between the pokemons that are not debilitated.
        It selects the one that has the best effectiveness, the one who can do the best vs. the 
        opponent Pokemon p. If there exist multiple pokemons with the same effectiveness, it chooses 
        the one with the highest level. It returns that pokemon.
    
    """ 
    
    def __init__(self, name:str, pokemon:list):
        """
         Assigns attributes to the object. 
         
         Parameters 
         ---------- 
         name : str 
             The name of the trainer. 
         pokemon : list 
             A list that contains Pokemon objects which belong to the Trainer. 
          
         Returns 
         ------- 
         None. 
         
         """ 
        self._name = name
        self._pokemon = pokemon
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value)>0 :
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
            
    @property
    def pokemon(self):
        return self._pokemon
    @pokemon.setter
    def pokemon(self, value: list):
        # Setter for the pokemon list
        if isinstance(value, list):
            self._pokemon = value
        else:
            raise ValueError("Pokemon must be a list")
        for p in self._pokemon:
            if not isinstance(p, Pokemon):
                raise TypeError("Elements of pokemon list must be Pokemon")
            
    def all_debilitated(self) -> bool:
        """
        Checks if all the pokemons of the list of the trainer (attribute pokemon) are debilitated, 
        it checks if HP is zero in all the pokemons.  
     
        Returns 
        -------- 
        bool
            True if all pokemons are debilitated (HP is zero), False otherwise.
            
        """ 
        all_debilitated = True
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                all_debilitated = False
                break
        return all_debilitated
    
    #return all(pokemon.is_debilitated() for pokemon in self._pokemon)
    
    
    def select_first_pokemon(self) -> Pokemon:
        """
        Chooses the first pokemon of the pokemon list that is not debilitated (HP is not zero).
        
        Returns 
        -------- 
        Pokemon
            The pokemon selected, or None if all the pokemons are debilitated     
            
        """ 
        
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                return pokemon 
        return None
    
    def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        """
        Chooses the next pokemon in the list between the pokemons that are not debilitated.
        It selects the one that has the best effectiveness, the one who can do the best vs. the 
        opponent Pokemon p. If there exist multiple pokemons with the same effectiveness, 
        it chooses the one with the highest level.
    
        Parameters 
        -------- 
        p : Pokemon 
            The opponent's Pokemon. 
            
        Returns 
        -------- 
        Pokemon
            The pokemon selected based on its effectiveness and level.  
            
        """ 
        pokemon_selected = self.select_first_pokemon()
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                if (pokemon.effectiveness(p) > pokemon_selected.effectiveness(p)):
                    pokemon_selected = pokemon
                elif pokemon.effectiveness(p) == pokemon_selected.effectiveness(p):
                    if pokemon.level > pokemon_selected.level :
                        pokemon_selected = pokemon
        return pokemon_selected
                
        
            
        
