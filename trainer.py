"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon

class Trainer(Pokemon):
    
    def __init__(self, name:str, pokemon:list):
        self._name = name
        self._pokemon = pokemon
        
    @property
    def name(self):
        return self._level
    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value)>0 :
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
            
    @property
    def pokemon(self):
        return self._level
    @pokemon.setter
    def pokemon(self, value: list):
        # Setter for the pokemon list
        if isinstance(value, list):
            self._pokemon = value
        else:
            raise ValueError("Pokemon must be a list")
            
    def all_debilitated(self) -> bool:
        all_debilitated = True
        for pokemon in self._pokemon:
            if pokemon._hp > 0:
                all_debilitated = False
                break
        return all_debilitated
    
    def select_first_pokemon(self) -> Pokemon:
        for pokemon in self._pokemon:
            if pokemon._hp > 0:
                return pokemon 
        return None
    
    def select_next_pokemon(self) -> Pokemon:
        pokemon_selected = self._select_first_pokemon()
        for pokemon in self._pokemon:
            if pokemon._hp > 0 and (pokemon._effectiveness() > pokemon_selected._effectiveness()):
                pokemon_selected = pokemon
        return pokemon_selected