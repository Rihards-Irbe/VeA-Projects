import random

class Heroes:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_attack(self):
        return self.attack
    
    def set_hp(self, hp):
        self.hp = hp

class Monsters:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_attack(self):
        return self.attack
    
    def set_hp(self, hp):
        self.hp = hp

def pretty_output(message: str, print_ending: bool=True, print_start: bool=True):

    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = '=' * max_length
    if(print_start):
        print(border)
    print(message)
    if(print_ending):
        print(border)

def validation(input_msg: str, expected_answer_1, expected_answer_2, error_msg: str, range: bool=False):

    validation = False
    while(validation == False):
        user_input = input(f"{input_msg}").lower()
        if(range == False):
            if(user_input == str(expected_answer_1).lower() or user_input == str(expected_answer_2).lower()):
                validation = True
                return user_input
        else:
            if(user_input.isnumeric() and int(user_input) >= expected_answer_1 and int(user_input) <= expected_answer_2):
                validation = True
                return user_input
        
        print(f"{error_msg}")

def fight(hero: object, monster: object) -> str:
    fight_ongoing = True
    while(fight_ongoing == True):
        hero_max_hp = hero.get_hp()
        monster_max_hp = monster.get_hp()
        print(f"{hero.get_name()}: HP {hero.get_hp()}/{hero_max_hp} | {monster.get_name()}: HP {monster.get_hp()}/{monster_max_hp}")
        if(random.randint(1, 20) > random.randint(1, 20)):
            user_input = int(validation(input_msg= f"Player's Turn: \n1. Attack\n2. Heal\nSelect an action (1 or 2): ",
                                    expected_answer_1=1,
                                    expected_answer_2=2,
                                    error_msg= 'Choose 1 or 2'))
            if(user_input == 1):
                print(f"{hero.get_name()} attacks {monster.get_name()} and deals {hero.get_attack()} damage.")
                monster.set_hp((monster.get_hp() - hero.get_attack()))
            else:
                if(hero_max_hp == hero.get_hp()):
                    hero_max_hp += 10
                hero.set_hp(hero.get_hp() + 10)
        else:
            print(f"{monster.get_name()} attacks {hero.get_name()} and deals {monster.get_attack()} damage.")
            hero.set_hp((hero.get_hp() - monster.get_attack()))
        
        if(monster.get_hp() < 0):
            print(f"{hero.get_name()} Won Against {monster.get_name()}")
            return "Hero Wins"
        elif(hero.get_hp() < 0):
            print(f"{hero.get_name()} Lost Against {monster.get_name()}")
            return f"Hero Loses"
        if(monster.get_hp() == 0 and hero.get_hp() == 0): #tie, bet itka skaitas, ka defeated
            print(f"{hero.get_name()} Won Against {monster.get_name()}")
            return f"Hero Wins"
        
heroes = []
monsters = []
user_done = False
current_monster = 0

heroes.append(Heroes(name="Royal Knight", hp=1, attack=400))
monsters.append(Monsters(name="Fire Dragon", hp=300, attack=50))

pretty_output(f"{monsters[0].get_name()} is quite strong he has {monsters[0].get_hp()} hp and deals {monsters[0].get_attack()} damage")
user_input = validation(input_msg= f'Would you like to add allies to help you in an upcoming battle: (y/n)',
                            expected_answer_1="y",
                            expected_answer_2="n",
                            error_msg= 'Choose y or n')

if(user_input == "y"):
    while(user_done == False):
        name_input = input("Choose ur new heroes name: ")
        dmg_input = int(validation(input_msg= f'Choose an attack value in range 30-40: ',
                                expected_answer_1=30,
                                expected_answer_2=40,
                                error_msg= 'Range must be from 30 to 40',
                                range=True))
        hp_input = int(validation(input_msg= f'Choose how much hp will this hero have in range 100-150: ',
                                expected_answer_1=100,
                                expected_answer_2=150,
                                error_msg= 'Range must be from 100-150',
                                range=True))
        
        heroes.append(Heroes(name=name_input, hp=hp_input, attack=dmg_input))

        user_input = validation(input_msg= f'Would you like to add another ally: (y/n)',
                            expected_answer_1="y",
                            expected_answer_2="n",
                            error_msg= 'Choose y or n')
        if(user_input.lower() == "n"):
            user_done = True

user_input = validation(input_msg= f'Would you like to add more monsters make the battle ur facing even harder: (y/n)',
                            expected_answer_1="y",
                            expected_answer_2="n",
                            error_msg= 'Choose y or n')
user_done = False
if(user_input == "y"):
    while(user_done == False):
        name_input = input("Choose ur new monsters name: ")
        dmg_input = int(validation(input_msg= f'Choose an attack value in range 40-500: ',
                                expected_answer_1=40,
                                expected_answer_2=500,
                                error_msg= 'Range must be from 40 to 500',
                                range=True))
        hp_input = int(validation(input_msg= f'Choose how much hp will this monster have in range 100-1000: ',
                                expected_answer_1=100,
                                expected_answer_2=1000,
                                error_msg= 'Range must be from 100-1000',
                                range=True))
        
        monsters.append(Monsters(name=name_input, hp=hp_input, attack=dmg_input))

        user_input = validation(input_msg= f'Would you like to add another monster?: (y/n)',
                            expected_answer_1="y",
                            expected_answer_2="n",
                            error_msg= 'Choose y or n')
        if(user_input.lower() == "n"):
            user_done = True

pretty_output(message=f"This is ur team:", print_ending = False)
for i in heroes:
    print(f"Name: {i.get_name()}, HP: {i.get_hp()}, Attack: {i.get_attack()}")

pretty_output(message=f"Fighting against these monsters:", print_start= False, print_ending=False)
for i in monsters:
    print(f"Name: {i.get_name()}, HP: {i.get_hp()}, Attack: {i.get_attack()}")

current_monster = 0

for i in range(len(heroes)):
    hero = heroes[i]
    while(hero.get_hp() > 0):
        pretty_output(message=f"Current Battle: {hero.get_name()} vs {monsters[current_monster].get_name()}", print_ending=False)
        print("")

        fight_outcome = fight(hero=hero, monster=monsters[current_monster])
        if(fight_outcome == "Hero Wins"):
            if(current_monster == len(monsters) - 1):
                pretty_output("The Heroes Won This Battle!")
                exit()
            else:
                current_monster += 1
                continue

        elif(fight_outcome == "Hero Loses"):
            break

if(current_monster < len(monsters)):
    pretty_output("The Monsters Won This Battle!")
