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
class Battle:


    def attack_order (self, p1:Pokemon, p2:Pokemon) -> tuple[Pokemon,Pokemon]:

        if p1.agility < p2.agility:
            return p2, p1
        else:
            return p1, p2

    def battle_begins (self, trainer1: Trainer, trainer2: Trainer):
        
        round_comb = 1
        loser = None 
        winner = None
        while not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            
            if round_comb == 1:
                p1 = trainer1.select_first_pokemon()
                p2 = trainer2.select_first_pokemon()
                
                print("=================================")
                print(f"Battle between: {trainer1.name} vs {trainer2.name} begins! \n{trainer1.name} chooses {p1.name}\n{trainer2.name} chooses {p2.name}")
                print("=================================")
            else: 
                if p1._name == loser._name:
                    p2 = winner
                    p1= trainer1.select_next_pokemon(p2)
                    print(f'{trainer1._name} chooses {p1.name}')
                elif p2._name == loser._name: 
                    p1= winner
                    p2= trainer2.select_next_pokemon(p1)
                    print(f'{trainer2._name} chooses {p2.name}')

            
            loser, winner = self.combat(p1,p2) 
            round_comb += 1
        if trainer1.all_debilitated():
            print("=" * 33)
            print(f"End of the Battle: {trainer2.name} wins!")
            print("=" * 33)
        elif trainer2.all_debilitated():
            print("=" * 33)
            print(f"End of the Battle: {trainer1.name} wins!")
            print("=" * 33)
            
            
    def combat(self,p1,p2) -> tuple[Pokemon, Pokemon]:
            round_num = 1
            while not (p1.is_debilitated() or p2.is_debilitated()):

                print (f"┌───────── Round {round_num} ─────────┐ \n Fighter 1: {p1._name} ({p1.pokemon_type}) Stats: Level: {p1.level}, ATT: {p1.strength}, DEF: {p1.defense}, AGI: {p1.agility}, HP: {p1.hp}/{p1.total_hp}. \n\n Figther 2: {p2.name} ({p2.pokemon_type}) Stats: Level: {p2.level}, ATT: {p2.strength}, DEF: {p2.defense}, AGI: {p2.agility}, HP: {p2.hp}/{p2.total_hp}. \n\n Actions") 

                attacker, defender = self.attack_order(p1, p2)
                
                self.attack(round_num, attacker, defender)
                
                if defender.is_debilitated():
                    print(f'{defender._name} is debilitated')
                    return defender, attacker
                
                self.attack(round_num, defender , attacker)
                
                if attacker.is_debilitated():
                    print(f'{attacker._name} is debilitated')
                    return attacker, defender
                    

                round_num += 1

    def attack (self, round_num, attacker, defender):
        
        if round_num%2 == 0: 
            damage = attacker.basic_attack(defender) 
            print(f"{attacker.name} uses a basic_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
            
        else:

            if  attacker._pokemon_type == 'Water': 
                damage = attacker.water_attack(defender)
                print(f"{attacker._name} uses a {attacker._pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender._hp})")
                
            elif attacker._pokemon_type == 'Fire':
                damage = attacker.fire_attack(defender)
                print(f"{attacker._name} uses a {attacker._pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender._hp})")
                ember_damage = attacker.embers(defender)
                print(f"{attacker._name} uses embers on {defender._name}! (Damage: -{ember_damage} HP: {defender._hp})")
            else:
                damage = attacker.grass_attack(defender)
                print(f"{attacker.name} uses a {attacker._pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender._hp})")
                healing = attacker.heal()
                print(f"{attacker.name} is healing! (Healing: +{healing} HP: {attacker._hp})")
            
    
        
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
        battle.battle_begins(trainer1, trainer2)



if __name__ == '__main__':
    main()
