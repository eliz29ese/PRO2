"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon

class Trainer():
    """
    A class of trainer objects representing players in a battle, each equipped with multiple Pokémon 
    that will be used in combats.
    
    Attributes 
    ---------- 
    name : str 
        The name of the trainer. 
    pokemon : list 
        A list with Pokémon objects that belong to the Trainer. 
        
    Methods 
    ------- 
    all_debilitated(self)): 
        Checks if all the Pokémon of the list of the trainer are debilitated.

    select_first_pokemon(self):
        Chooses the first Pokémon of the pokemon list that is not debilitated.
    
    select_next_pokemon(self, p:Pokemon):
        Chooses the next Pokémon in the list between the Pokémon that are not debilitated, 
        the most effective one, and among those, the one with the highest level.
    
    """ 
    
    def __init__(self, name:str, pokemon:list):
        """
         Creates a Trainer with the attributes given. 
         
         Parameters 
         ---------- 
         name : str 
             The name of the trainer. 
         pokemon : list 
             A list that contains Pokémon objects which belong to the Trainer. 
          
         Returns 
         ------- 
         None. 
         
         """ 
        self._name = name
        self._pokemon = pokemon
        
    @property
    def name(self):
        """
        Gets the name of the Trainer.
        
        Returns
        -------
        str
            The name of the Trainer.
        """
        return self._name
    @name.setter
    def name(self, value: str):
        """
       Set the name of the Trainer.
    
       Parameters
       ----------
       value : str
           The new name for the Trainer.
    
       Raises
       ------
       ValueError
           If the provided value is not a non-empty string.
       """
        # Setter for the name
        if isinstance(value, str) and len(value)>0 :
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
            
    @property
    def pokemon(self):
        """
        Gets the pokemon list of the Trainer.
        
        Returns
        -------
        list
            The pokemon list of the Trainer.
        """
        return self._pokemon
    @pokemon.setter
    def pokemon(self, value: list):
        """
       Set the pokemon list of the Trainer, containing Pokémon objects.
    
       Parameters
       ----------
       value : list
           The new list containing Pokémon objects for the Trainer.
    
       Raises
       ------
       ValueError
           If the provided value is not a list.
       TypeError
           If the provided values inside the list are not Pokémon objects.
       """
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
        Checks if all the Pokémon of the list of the trainer are debilitated, 
        it checks if HP is zero in all the Pokémon.  
     
        Returns 
        -------- 
        bool
            True if all Pokémon are debilitated (HP is zero), False otherwise.
            
        """ 
        all_debilitated = True
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                all_debilitated = False
                break
        return all_debilitated
    
    
    def select_first_pokemon(self) -> Pokemon:
        """
        Chooses the first Pokémon of the pokemon list that is not debilitated (HP is not zero).
        
        Returns 
        -------- 
        Pokemon
            The Pokémon selected, or None if all the Pokémon are debilitated     
            
        """ 
        
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                return pokemon 
        return None
    
    def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        """
        Chooses the next Pokémon in the list between the Pokémon that are not debilitated.
        It selects the one that has the best effectiveness against the opponent. If there exist
        multiple Pokémon with the same effectiveness, it chooses the one with the highest level.
        
        Preconditions
        -------------
        At least one Pokémon of the Trainer is not debilitated.

        Parameters 
        -------- 
        p : Pokemon 
            The opponent's Pokémon. 
            
        Returns 
        -------- 
        Pokemon
            The Pokémon chosen based on its effectiveness and level.  
            
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
                
        
            
        
        
