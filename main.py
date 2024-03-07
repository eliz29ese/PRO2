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
    
    """Class representing a battle between trainers and their Pokémon.
    
    This class contains methods to simulate a battle between two trainers and their Pokémon.
    To start a battle, an instance of this class must be created and the "battle_begins" method must be called.
    All other methods necessary to carry out the battle are called internally by "battle_begins".
    
    Battle Premises:
        - The Battle consists of combats, which in turn are composed of rounds.
        - A battle ends when all of a trainer's Pokémon are debilitated.
        - A combat ends when one of the Pokémon is debilitated.
        - A round ends when both Pokémon attack or if the defending Pokémon is debilitated in the first attack.
    
    Usage Example:
        battle_instance = Battle() \n
        battle_instance.battle_begins(trainer1, trainer2)
    
    Attributes
    ----------
    The instance of the class has no initial attributes.
    
    Methods
    -------
    Public Methods:
        battle_begins(self, trainer1: Trainer, trainer2: Trainer) -> None:
            Initiates the battle between two trainers and their respective Pokémon.
    
    Private Methods:
        _combat(self, p1, p2, lista_p:list) -> tuple[Pokemon, Pokemon]:
            Simulates a combat between two Pokémon.
        
        _attack_order(self, p1:Pokemon, p2:Pokemon) -> tuple[Pokemon, Pokemon]:
            Determines the attack order between two Pokémon based on their agility.
    
        _attack(self, attacker:Pokemon, defender:Pokemon, round_num:int) -> tuple[int, int]:
            Simulates the attack of an attacker Pokémon to the defender Pokémon.
    
        _pandas_stats(self, lista_p: list) -> None:
            Calculates battle statistics using the pandas library.
        
    """

    def battle_begins (self, trainer1: Trainer, trainer2: Trainer) -> None:
        
        """Initiates the battle between two trainers and their respective Pokémon.
        
        Method Characteristics: 
            - The battle continues until all Pokémon of one of the trainers are debilitated.
            - Each battle consists of one or more combats:
                - In the first combat, the first Pokémon of each trainer is selected (using 'select_first_pokemon()').
                - After the first combat, trainers select a new Pokémon (using 'select_next_pokemon()') if their Pokémon loses the previous combat. 
                  If they win, they will use the same Pokémon for the next combats until it gets debilitated.
            - If one of the trainers has all their Pokémon debilitated, the other trainer is declared the winner of the battle.
            - At the end of the battle, the battle statistics are calculated and displayed using '_pandas_stats()' with the data collected in 'data_list_p'.

        Parameters:
        -----------
        trainer1 : Trainer
            Instance of Trainer that will have a battle with trainer2.
        trainer2 : Trainer
            Instance of Trainer that will have a battle with trainer1.
    
        Returns:
        --------
        None
                 
        Notes:
        -----
        - During the execution of this function, several informative messages are printed, including:
            - The start of the battle between the trainers and the first Pokémon of each trainer.
            - Each time a trainer selects a new Pokémon.
            - The start and number of combats of the battle.
            - The name of the winner of the battle.
        - For more information about 'select_first_pokemon()' and 'select_next_pokemon()' methods, please refer to the documentation of the Trainer class.
        - To execute the combats and determine who was the combat_loser and the combat_winner of the previous round, the _combat() method is used.
        
        """
        
        data_list_p =[]
        combat_num = 1
        combat_loser = None 
        combat_winner = None
        
        while not(trainer1.all_debilitated() or trainer2.all_debilitated()):
            
            if combat_num == 1:
                p1 = trainer1.select_first_pokemon()
                p2 = trainer2.select_first_pokemon()
                
                print("=================================")
                print(f"Battle between: {trainer1.name} vs {trainer2.name} begins! \n{trainer1.name} chooses {p1.name}\n{trainer2.name} chooses {p2.name}")
                print("=================================")
            else: 
                if p1._name == combat_loser.name:
                    p2 = combat_winner
                    #pokemon_trainer1
                    p1= trainer1.select_next_pokemon(p2)
                    print(f'{trainer1.name} chooses {p1.name}')
                elif p2._name == combat_loser._name: 
                    p1= combat_winner
                    p2= trainer2.select_next_pokemon(p1)
                    print(f'{trainer2.name} chooses {p2.name}')
                    
            print('-'*33)
            print(f'     Combat number {combat_num} begins')
            print('-'*33)

            combat_loser, combat_winner = self._combat(p1,p2, data_list_p) 
            combat_num += 1
            
        if trainer1.all_debilitated():
            print("=" * 43)
            print(f"End of the Battle: {trainer2.name} wins!")
            print("=" * 43)

        elif trainer2.all_debilitated():
            print("=" * 43)
            print(f"End of the Battle: {trainer1.name} wins!")
            print("=" * 43)
        
        self._pandas_stats(data_list_p)
    
            
    def _combat (self,pokemon_t1, pokemon_t2, data_list_p:list ) -> tuple[Pokemon, Pokemon]: 
            
            """Simulates a combat between two Pokémon.
                    
            Combat Premises:
                - A combat ends when one of the Pokémon in battle is debilitated.
                - Each combat consists of one or more rounds.
                    - Each round can have a maximum of two attack actions, one per Pokémon.
                    - If a Pokémon is debilitated at the beginning of a round, it withdraws, and the round and the combat end.
                    - Therefore, a round can have only one attack action if one Pokémon debilitates the opponent at the beginning of the round.
                    
            Method Characteristics:
                - At the beginning of each round, a message with the information of the two Pokémon in combat will be printed.
                - The round number starts at 1 for each combat.
                    
            Parameters:
            -----------
            pokemon_t1 : Pokemon
                Pokémon instance from the first trainer. This will face pokemon_t2 in combat.
            pokemon_t2 : Pokemon
                Pokémon instance from the second trainer. This will face pokemon_t2 in combat.
            data_list_p : list
                Empty list defined in the battle_begins() method.
                After each attack, essential information about it is added to the list, which is then used to calculate battle statistics.
                    
            Returns:
            --------
            tuple[Pokemon, Pokemon]
                - The first element of the tuple (index 0) is the Pokémon that lost the combat.
                - The second element of the tuple (index 1) is the Pokémon that won the combat.
                    
            Note:
            -----
            This method calls _attack() to execute the attacks and _attack_order() to determine who will be the first to attack (attacker) and who will be the second to attack (defender).
            """
            round_num = 1

            while not (pokemon_t1.is_debilitated() or pokemon_t2.is_debilitated()):

                print (f" \n ┌───────── Round {round_num} ─────────┐ \n Fighter 1: {pokemon_t1.name} ({pokemon_t1.pokemon_type}) Stats: Level: {pokemon_t1.level}, ATT: {pokemon_t1.strength}, DEF: {pokemon_t1.defense}, AGI: {pokemon_t1.agility}, HP: {pokemon_t1.hp}/{pokemon_t1.total_hp}. \n\n Figther 2: {pokemon_t2.name} ({pokemon_t2.pokemon_type}) Stats: Level: {pokemon_t2.level}, ATT: {pokemon_t2.strength}, DEF: {pokemon_t2.defense}, AGI: {pokemon_t2.agility}, HP: {pokemon_t2.hp}/{pokemon_t2.total_hp}. \n\n Actions") 
            
                attacker, defender = self._attack_order(pokemon_t1, pokemon_t2)
                
                #Primer ataque de la ronda
                damage, healing = self._attack(attacker, defender, round_num)
                data_list_p.append([attacker.name, damage, attacker.pokemon_type, defender.pokemon_type, healing])
                
                if defender.is_debilitated():
                    print(f'{defender.name} is debilitated')
                    return defender, attacker
                
                #Segundo ataque de la ronda, si procede 
                damage, healing = self._attack(defender , attacker, round_num)
                data_list_p.append([defender.name, damage, defender.pokemon_type, attacker.pokemon_type, healing])
                
                if attacker.is_debilitated():
                    print(f'{attacker.name} is debilitated')
                    return attacker, defender
                    

                round_num += 1
    
    def _attack_order (self, pokemon_t1:Pokemon, pokemon_t2:Pokemon) -> tuple[Pokemon,Pokemon]:
        
        """Determines the attack order between two Pokémon based on their agility.
    
        The Pokémon with higher agility attacks first in the round.
        If the Pokémon have equal agility, priority is given to the Pokémon from the first trainer.
    
        Parameters
        ----------
        pokemon_t1 : Pokemon
            One of the Pokémon instances from the first trainer.
        pokemon_t2 : Pokemon
            One of the Pokémon instances from the second trainer. 
    
        Returns
        -------
        tuple[Pokemon, Pokemon]
            The result of comparing the 'agility' attribute of the Pokémon.
            The Pokémon at index 0 in the tuple attacks first, followed by the Pokémon at index 1.
    
        Note
        ----
        pokemon_t1 and pokemon_t2 were already selected from the trainer's Pokémon list in the battle_begins() method.
        """

        if pokemon_t1.agility < pokemon_t2.agility:
            return pokemon_t2, pokemon_t1
        else:
            return pokemon_t1, pokemon_t2 

    def _attack (self, attacker:Pokemon , defender:Pokemon, round_num:int) -> tuple[int, int]:
        
        """Simulates an attack from the attacker Pokémon to the defender Pokémon.
    
        Characteristics of this method:
            - The type of attack to be used by the Pokémon depends on the round number and the attacker's type
                - In even rounds, attacker use their basic attack.
                - In odd rounds, attacker use their class-specific attack.
            - If the attacker is of type 'Grass', it heals itself after using a class-specific attack (using 'heal()').
            - If the attacker is of type 'Fire', it performs an additional embers attack after its class-specific attack (using 'embers()'),
              provided that the defender is not debilitated.
            - Attacks, healing, and embers are part of the round's actions, which are recorded and displayed on the screen with their essential information.
    
        Parameters:
        -----------
        attacker : Pokemon
            The Pokémon attacking the defender.
        defender : Pokemon
            The Pokémon being attacked.
        round_num : int 
            The number of the round in which the attack takes place.
    
        Returns:
        --------
        tuple[int, int]
            - The first element of the tuple (index 0) represents the damage caused by the attacks.
            - The second element of the tuple (index 1) represents the amount of healing obtained.
                  - For Pokémon that are not of type 'Grass', healing is 0.
                  - For Pokémon of type 'Grass', healing represents the amount of life restored using the 'heal()' method.
    
        Note:
        -----
        For more information about 'basic_attack()', class-specific attacks ('water_attack()', 'fire_attack()', 'grass_attack()'),
        the 'heal()' method, and the 'embers()' method, please refer to the documentation of the Pokemon class and its subclasses.
        """

        healing = 0 
        if round_num%2 == 0: 
            damage = attacker.basic_attack(defender) 
            print(f"-{attacker.name} uses a basic_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
            
        else:

            if  attacker.pokemon_type == 'Water': 
                damage = attacker.water_attack(defender)
                print(f"-{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                
            elif attacker.pokemon_type == 'Fire':
                damage = attacker.fire_attack(defender)
                print(f"-{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                if not defender.is_debilitated():
                    ember_damage = attacker.embers(defender)
                    damage += ember_damage 
                    print(f"-{attacker.name} uses embers on {defender.name}! (Damage: -{ember_damage} HP: {defender.hp})")
            else:
                damage = attacker.grass_attack(defender)
                print(f"-{attacker.name} uses a {attacker.pokemon_type}_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                healing = attacker.heal()
                print(f"-{attacker.name} is healing! (Healing: +{healing} HP: {attacker.hp})")
                
        return damage, healing
    
    def _pandas_stats (self, data_list_p: list) -> None:

        """Calculates battle statistics using the pandas library.

        This method computes The mean and standard deviation for each group formed in the DataFrame.
        The statistics are displayed at the end of the battle and include:
            1. Average **damage** caused by each **individual** Pokémon.
            2. Average **damage** caused by Pokémon of **each type**.
            3. Average **damage** inflicted by **each type** of Pokémon **to** each of **its opponent types**.
            4. Average **healing** performed by each **individual** Pokémon.
            5. Average **healing** performed by Pokémon of **each type**.

        Parameters:
        -----------
        data_list_p : list
            A list containing attacks per combat data. 
            This data is used to create a DataFrame for calculating the statistics.

        Returns:
        --------
        None
            All resulting statistics are printed in the screen.

        Note:
        -----
        Since _pandas_stats() is called through battle_begins(), the information contained in data_list_p is appended for each round and attack in the battle.
        """
        
        #Create a DataFrame using the combat list data 
        data = pandas.DataFrame(data_list_p, columns=["Pokemon_name","Damage", 'Pokemon_type', 'Opponent_type', 'Healing'])
        print(data)
        
        #Statistics for individual Pokémon damage
        group_col = "Pokemon_name"
        target_col = "Damage" 
        single_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "          Individual Damage      ", '\n',  "*"*37 )
        print (single_stats)
        
        #Statistics for damage grouped by Pokémon type
        group_col = "Pokemon_type"
        target_col = "Damage"  
        type_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "     Damage group by Pokemon Type     ", '\n',  "*"*37 )
        print(type_stats)
        
        #Statistics for damage inflicted by each type of Pokémon to each of its opponent types
        group_col = ["Pokemon_type", 'Opponent_type']
        target_col = "Damage" 
        type2_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*57, '\n', "Pokemon damage to Opponent pokemon group by Pokemon Type     ", '\n',  "*"*57 )
        print(type2_stats)
        
        #Statistics for individual Pokémon healing
        group_col = "Pokemon_name"
        target_col = "Healing"  
        healing_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "          Individual Healing      ", '\n',  "*"*37 )
        print(healing_stats)
        
        #Statistics for healing grouped by Pokémon type
        group_col = "Pokemon_type"
        target_col = "Healing" 
        healing_type_stats = data.groupby(group_col).agg({target_col :["mean","std"]})
        print('\n', "*"*37, '\n', "     Healing group by Pokemon Type     ", '\n',  "*"*37 )
        print(healing_type_stats)
    
        
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
