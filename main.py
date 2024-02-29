import sys
from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon
from trainer import Trainer

class PokemonSimulator:
    """A class that simulates Pokemon trainers and their Pokemon."""

    def create_trainer_and_pokemons(self, text: str):
        """
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.
        
        Returns:
        None: The function is currently set up to return None. Intended to return a Trainer instance in future development.
        """

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0] # Extracting the pokemon's name
            details = parts[1].strip(')').split(', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            
            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = float(details[6].split(': ')[1])
                # TODO: Implement creation of a FirePokemon
                pokemon_name = FirePokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, temperature)
                pokemons.append(pokemon_name)
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, temperature: {temperature} ")
            elif pokemon_type == 'Grass':
                # TODO: Implement creation of a GrassPokemon
                healing = float(details[6].split(': ')[1])
                # Printing the attributes for now
                pokemon_name = GrassPokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, healing)
                pokemons.append(pokemon_name)
                print (f"name: {pokemon_name},  level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, healing: {healing} ")
            elif pokemon_type == 'Water':
                surge_mode = False
                # TODO: Implement creation of a WaterPokemon
                pokemon_name = WaterPokemon(pokemon_name, level, strength, defense, hp, total_hp, agility)
                pokemons.append(pokemon_name)
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, surge_mode: {surge_mode} ")
            else: 
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")
        
        trainer_name = Trainer(trainer_name, pokemons)

        # Reminder to implement the instance creation of Trainer
        # Function is intended to return a Trainer instance in future development
        return trainer_name

    def parse_file(self, text: str):
        """
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        """

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2




class Battle():
    
    def select_first_pokemons(self, trainer1, trainer2):
        if not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            p1 = trainer1.select_first_pokemon()
            p2 = trainer2.select_first_pokemon()
        return trainer1, p1, trainer2, p2
    
    
    def new_battle(self, attacker, defender, X):
        while not (attacker.is_debilitated() or defender.is_debilitated()):
             
            print (f"┌───────── Round {X} ─────────┐ \n Fighter 1: {attacker.name} ({attacker.pokemon_type}) Stats: Level: {attacker.level}, ATT: {attacker.strength}, DEF: {attacker.defense}, AGI: {attacker.agility}, HP: {attacker.hp}/{attacker.total_hp}. \n\n Figther 2: {defender.name} ({defender.pokemon_type}) Stats: Level: {defender.level}, ATT: {defender.strength}, DEF: {defender.defense}, AGI: {defender.agility}, HP: {defender.hp}/{defender.total_hp}. \n\n Actions") 
            
            
            if X%2 == 1: 
                damage = attacker.basic_attack(defender) 
                print(f"{attacker._name} uses a basic_attack on {defender._name}! (Damage: -{damage} HP: {defender._hp}) ")

            else:
                
                if  attacker._pokemon_type == 'Water': 
                    damage = attacker.water_attack(defender)
                    
                elif attacker._pokemon_type == 'Fire':
                    damage = attacker.fire_attack(defender)
                    damage2 = attacker._embers()
                    print(f"- {attacker.name} uses embers on {defender.name}! (Damage: -{damage2} HP: {defender.hp}) ")
                else:
                    damage = attacker.grass_attack(defender)
                    healing = attacker.heal()
                    print(f"{attacker.name} is healing! (Healing: {healing}+HP: {attacker.hp}) ")
                print(f"{attacker._name} uses a {attacker._pokemon_type}_attack on {defender._name}! (Damage: -{damage} HP: {defender._hp}) ")
            X+=1
        return(X)
    def choose_attacker_defender(self, trainer1, p1, trainer2, p2):
        if not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            
            if p1.agility < p2.agility:
                attacker_trainer, attacker, defender_trainer, defender =  trainer2, p2, trainer1, p1
            else:
                attacker_trainer, attacker, defender_trainer, defender = trainer1, p1, trainer2, p2
            return(attacker_trainer, attacker, defender_trainer, defender)
                
    def begin_battle(self, trainer1, p1, trainer2, p2):
        print("=================================")
        print(f"Battle between: {trainer1.name} vs {trainer2.name} begins! \n{trainer1.name} chooses {p1.name}\n{trainer2.name} chooses {p2.name}")
        print("=================================")
        
        attacker_trainer, attacker, defender_trainer, defender = self.choose_attacker_defender(trainer1, p1, trainer2, p2)
        X = 1
        while not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            
            X = self.new_battle(attacker, defender, X)
                
                
            if defender.is_debilitated():
                defender = defender_trainer.select_next_pokemon()
                

        if trainer1.all_debilitated():
            winner = trainer2
        else:
            winner = trainer1
        print("=================================")
        print(f"End of the Battle: {winner.name} wins! ")
        print("=================================")







def main():

    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        print ("""TODO: Implement the rest of the practice from here. Define classes and functions and
        maintain the code structured, respecting the object-oriented programming paradigm""")
        
    battle = Battle()
    
    trainer1, p1, trainer2, p2 = battle.select_first_pokemons(trainer1, trainer2)
    
    battle.begin_battle(trainer1, p1, trainer2, p2)
        
        
     
if __name__ == '__main__':
    main()   
        
