"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon

class Trainer():
    
    def __init__(self, name:str, pokemon:list):
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
        all_debilitated = True
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                all_debilitated = False
                break
        return all_debilitated
    
    #return all(pokemon.is_debilitated() for pokemon in self._pokemon)
    
    
    def select_first_pokemon(self) -> Pokemon:
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                return pokemon 
        return None
    
    def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        pokemon_selected = self.select_first_pokemon()
        for pokemon in self.pokemon:
            if pokemon.hp > 0:
                if (pokemon.effectiveness(p) > pokemon_selected.effectiveness(p)):
                    pokemon_selected = pokemon
                elif pokemon.effectiveness(p) == pokemon_selected.effectiveness(p):
                    if pokemon.level > pokemon_selected.level :
                        pokemon_selected = pokemon
        return pokemon_selected
                
        
            
        
