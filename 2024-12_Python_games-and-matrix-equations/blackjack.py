import random

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

def pretty_output(message: str):

    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = '=' * max_length
    print(border)
    print(message)
    print(border)

def randomly_choose_a_card():

    card_suits = ["♥", "♦", "♠", "♣"]
    random_card = random.randint(1, 13)
    if(random_card <= 9):
        return f'{random_card}{card_suits[random.randint(0, 3)]}'
    if(random_card == 10):
        return f'J{card_suits[random.randint(0, 3)]}'
    elif(random_card == 11):
        return f'Q{card_suits[random.randint(0, 3)]}'
    elif(random_card == 12):
        return f'K{card_suits[random.randint(0, 3)]}'
    elif(random_card == 13):
        return f'A{card_suits[random.randint(0, 3)]}'

def count_points(card_list: list) -> int:
    total_points = 0
    for i in card_list:
        current_card = i[:-1]
        if(current_card == "K" or current_card == "Q" or current_card == "J"):
            total_points += 10
        elif(current_card.isnumeric()):
            total_points += int(current_card)
        elif(current_card == "A"):
            if(total_points + 11 > 21):
                total_points += 1
            elif(total_points + 11 <= 21):
                total_points += 11
    
    return total_points

life_savings = 1000
game_running = True
AI_cards = []
user_cards = []
AI_first_card = False
bet_placed = False
user_input = ""

while(game_running == True):
    if life_savings <= 0:
        print("Tev beidzās nauda, tāpēc nevari vairs spēlēt")
        game_running = False
        break

    while(user_input != "n"):
        if(bet_placed == False):
            placed_bet = int(validation(input_msg= f'Tev pieejamā nauda: {life_savings}, cik vēlies betot: ',
                                expected_answer_1= 1,
                                expected_answer_2= life_savings,
                                error_msg= 'Lūdzu ievadi pareizu naudas daudzumu',
                                range= True))
            bet_placed = True

        user_cards.append(randomly_choose_a_card())
        if(count_points(user_cards) > 21):
            break

        if(AI_first_card == False):
            AI_cards.append(randomly_choose_a_card())
            AI_first_card = True

        pretty_output(f"Tavas kārtis: {user_cards}, Tavs rezultāts: {count_points(user_cards)} \nDatora pirmā kārts: {AI_cards}, rezultāts: {count_points(AI_cards)}")

        user_input = validation(input_msg= f"'y' lai iegūtu vēlvienu kārti, vai 'n' lai beigtu: ",
                                expected_answer_1= "y",
                                expected_answer_2= "n",
                                error_msg= 'Lūdzu ievadi y vai n',)
        
        if(user_input == "n"):
            break

    while(count_points(AI_cards) < 21):
        if(count_points(AI_cards) > count_points(user_cards) or count_points(user_cards) > 21):
            break
        AI_cards.append(randomly_choose_a_card())

    if(count_points(user_cards) > 21):
        life_savings -= placed_bet
        pretty_output(f"Tava pēdējā roka: {user_cards}, beigu rezultāts: {count_points(user_cards)} \nDatora pēdējā roka: {AI_cards}, rezultāts: {count_points(AI_cards)}\nNauda: {life_savings}")
        user_input = validation(input_msg="Tev pārgāja pāri. Tu zaudēji. Vai vēlaties spēlēt vēlreiz? (y/n): ",
                                expected_answer_1="y",
                                expected_answer_2="n",
                                error_msg='Lūdzu ievadi y vai n')
        
    elif(count_points(AI_cards) > 21):
        life_savings += placed_bet
        pretty_output(f"Tava pēdējā roka: {user_cards}, beigu rezultāts: {count_points(user_cards)} \nDatora pēdējā roka: {AI_cards}, rezultāts: {count_points(AI_cards)}\nNauda: {life_savings}")
        user_input = validation(input_msg="Datoram pārgāja pāri. Tu uzvarēji. Vai vēlaties spēlēt vēlreiz? (y/n): ",
                                expected_answer_1="y",
                                expected_answer_2="n",
                                error_msg='Lūdzu ievadi y vai n')
        
    elif(count_points(user_cards) > count_points(AI_cards)):
        life_savings += placed_bet
        pretty_output(f"Tava pēdējā roka: {user_cards}, beigu rezultāts: {count_points(user_cards)} \nDatora pēdējā roka: {AI_cards}, rezultāts: {count_points(AI_cards)}\nNauda: {life_savings}")
        user_input = validation(input_msg="Tu uzvarēji! Vai vēlaties spēlēt vēlreiz? (y/n): ",
                                expected_answer_1="y",
                                expected_answer_2="n",
                                error_msg='Lūdzu ievadi y vai n')
        
    elif(count_points(user_cards) < count_points(AI_cards)):
        life_savings -= placed_bet
        pretty_output(f"Tava pēdējā roka: {user_cards}, beigu rezultāts: {count_points(user_cards)} \nDatora pēdējā roka: {AI_cards}, rezultāts: {count_points(AI_cards)}\nNauda: {life_savings}")
        user_input = validation(input_msg="Tu zaudēji. Vai vēlaties spēlēt vēlreiz? (y/n): ",
                                expected_answer_1="y",
                                expected_answer_2="n",
                                error_msg='Lūdzu ievadi y vai n')
        
    else:
        pretty_output(f"Tava pēdējā roka: {user_cards}, beigu rezultāts: {count_points(user_cards)} \nDatora pēdējā roka: {AI_cards}, rezultāts: {count_points(AI_cards)}\nNauda: {life_savings}")
        user_input = validation(input_msg="Neizšķirts! Vai vēlaties spēlēt vēlreiz? (y/n): ",
                                expected_answer_1="y",
                                expected_answer_2="n",
                                error_msg='Lūdzu ievadi y vai n')

    if(user_input.lower() == "y"):
        AI_cards = []
        user_cards = []
        AI_first_card = False
        bet_placed = False
        user_finished = False
    else:
        game_running = False
        