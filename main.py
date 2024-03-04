import sys
from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon
from trainer import Trainer
import pandas
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


    def attack_order (self, p1:Pokemon, p2:Pokemon) -> tuple:

        if p1.agility < p2.agility:
            return p2, p1
        else:
            return p1, p2 
        
    def pandas_stats (self, lista_p: list) -> None: 
        data = pandas.DataFrame(lista_p, columns=["Pokemon_names","Damage", 'Pokemon_type', 'Opponent_type', 'Healing'])
        print(data)
        

        group_col = "Pokemon_names"
        target_col = "Damage" #sobre cual realizar la operacion 
        single_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "          Individual Damage      ", '\n',  "*"*37 )
        print (single_stats)
        
        group_col = "Pokemon_type"
        target_col = "Damage" #sobre cual realizar la operacion 
        type_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "     Damage group by Pokemon Type     ", '\n',  "*"*37 )
        print(type_stats)
        
        group_col = ["Pokemon_type", 'Opponent_type']
        target_col = "Damage" #sobre cual realizar la operacion 
        type2_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*57, '\n', "Pokemon damage to Opponent pokemon group by Pokemon Type     ", '\n',  "*"*57 )
        print(type2_stats)
        
        group_col = "Pokemon_names"
        target_col = "Healing" #sobre cual realizar la operacion 
        healing_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "          Individual Healing      ", '\n',  "*"*37 )
        print(healing_stats)
        
        group_col = "Pokemon_type"
        target_col = "Healing" #sobre cual realizar la operacion 
        healing_type_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "     Healing group by Pokemon Type     ", '\n',  "*"*37 )
        print(healing_type_stats)


    def battle_begins (self, trainer1: Trainer, trainer2: Trainer):
        lista_p =[]
        comb_num = 1
        loser = None 
        winner = None
        while not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            
            if comb_num == 1:
                p1 = trainer1.select_first_pokemon()
                p2 = trainer2.select_first_pokemon()
                
                print("=================================")
                print(f"Battle between: {trainer1.name} vs {trainer2.name} begins! \n{trainer1.name} chooses {p1.name}\n{trainer2.name} chooses {p2.name}")
                print("=================================")
            else: 
                if p1.name == loser.name:
                    p2 = winner
                    p1= trainer1.select_next_pokemon(p2)
                    print(f'{trainer1.name} chooses {p1.name}')
                elif p2.name == loser.name: 
                    p1= winner
                    p2= trainer2.select_next_pokemon(p1)
                    print(f'{trainer2.name} chooses {p2.name}')
                    
            print('*'*33)
            print(f'     Combat number {comb_num} begins')
            print('*'*33)

            loser, winner = self.combat(p1,p2, lista_p) 
            comb_num += 1
        if trainer1.all_debilitated():
            print("=" * 43)
            print(f"End of the Battle: {trainer2.name} wins!")
            print("=" * 43)

        elif trainer2.all_debilitated():
            print("=" * 43)
            print(f"End of the Battle: {trainer1.name} wins!")
            print("=" * 43)
        
        self.pandas_stats(lista_p)

            
            
    def combat(self,p1 ,p2, lista_p:list ) -> tuple:
            round_num = 1

            while not (p1.is_debilitated() or p2.is_debilitated()):

                print (f" \n ┌───────── Round {round_num} ─────────┐ \n Fighter 1: {p1.name} ({p1.pokemon_type}) Stats: Level: {p1.level}, ATT: {p1.strength}, DEF: {p1.defense}, AGI: {p1.agility}, HP: {p1.hp}/{p1.total_hp}. \n\n Figther 2: {p2.name} ({p2.pokemon_type}) Stats: Level: {p2.level}, ATT: {p2.strength}, DEF: {p2.defense}, AGI: {p2.agility}, HP: {p2.hp}/{p2.total_hp}. \n\n Actions") 

                attacker, defender = self.attack_order(p1, p2)
                
                damage, healing = self.attack(round_num, attacker, defender)
                
                lista_p.append([attacker.name, damage, attacker.pokemon_type, defender.pokemon_type, healing])
                
                if defender.is_debilitated():
                    print(f'{defender.name} is debilitated')
                    return defender, attacker
                
                damage, healing = self.attack(round_num, defender , attacker)
                
                lista_p.append([defender.name, damage, defender.pokemon_type, attacker.pokemon_type, healing])
                
                if attacker.is_debilitated():
                    print(f'{attacker.name} is debilitated')
                    return attacker, defender
                    

                round_num += 1

    def attack (self, round_num, attacker, defender):
        healing = 0 
        if round_num%2 == 0: 
            damage = attacker.basic_attack(defender) 
            print(f"{attacker.name} uses a basic_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
            
        else:

            if  attacker.pokemon_type == 'Water': 
                damage = attacker.water_attack(defender)
                print(f"{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                
            elif attacker.pokemon_type == 'Fire':
                damage = attacker.fire_attack(defender)
                print(f"{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                ember_damage = attacker.embers(defender)
                damage += ember_damage 
                print(f"{attacker.name} uses embers on {defender.name}! (Damage: -{ember_damage} HP: {defender.hp})")
            else:
                damage = attacker.grass_attack(defender)
                print(f"{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                healing = attacker.heal()
                print(f"{attacker.name} is healing! (Healing: +{healing} HP: {attacker.hp})")
                
        return damage, healing
    
        
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
