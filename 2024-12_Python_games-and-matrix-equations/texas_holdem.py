import random

def generate_deck():

    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ["♥", "♦", "♠", "♣"]
    deck = []
    for value in vals:
        for suit in card_suits:
            deck.append(f"{value}{suit}")
    random.shuffle(deck)
    return deck

def pretty_output(message: str):

    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = '=' * max_length
    print(border)
    print(message)
    print(border)

def deal_cards(deck, amount_of_cards):
    
    dealt_cards = []
    for i in range(amount_of_cards):
        dealt_cards.append(deck.pop())
    return dealt_cards

def evaluate_hand(hand):

    value_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = [i for i in range(2, 15)]
    suits = [0, 0, 0, 0]
    counts = [0] * 13

    for card in hand:
        value, suit = card[:-1], card[-1]
        value_index = value_labels.index(value)
        counts[value_index] += 1
        suit_index = ["♥", "♦", "♠", "♣"].index(suit)
        suits[suit_index] += 1

    is_flush = max(suits) >= 5

    sorted_values = []
    for i, count in enumerate(counts):
        if count > 0:
            sorted_values.extend([values[i]] * count)
    sorted_values.sort(reverse=True)

    is_straight = False
    for i in range(len(sorted_values) - 4):
        if sorted_values[i] - sorted_values[i + 4] == 4:
            is_straight = True
            break
    if set([14, 2, 3, 4, 5]).issubset(sorted_values):  # Kkads special case
        is_straight = True

    if is_straight and is_flush:
        return 9  # Straight Flush
    elif 4 in counts:
        return 8  # Four of a Kind
    elif 3 in counts and 2 in counts:
        return 7  # Full House
    elif is_flush:
        return 6  # Flush
    elif is_straight:
        return 5  # Straight
    elif 3 in counts:
        return 4  # Three of a Kind
    elif counts.count(2) == 2:
        return 3  # Two Pair
    elif 2 in counts:
        return 2  # One Pair
    else:
        return 1  # High Card

deck = generate_deck()
player_1_hand = deal_cards(deck, 2)
player_2_hand = deal_cards(deck, 2)

pretty_output(f"Player 1's hand: {player_1_hand} \nPlayer 2's hand: {player_2_hand}")

flop = deal_cards(deck, 3)
turn = deal_cards(deck, 1)
river = deal_cards(deck, 1)

print("Flop:", flop)
print("Turn:", turn)
print("River:", river)

player_1_combined = player_1_hand + flop + turn + river
player_2_combined = player_2_hand + flop + turn + river

pretty_output(f"Player 1's full hand: {player_1_combined} \nPlayer 2's full hand: {player_2_combined}")

player_1_score = evaluate_hand(player_1_combined)
player_2_score = evaluate_hand(player_2_combined)

pretty_output(f"Player 1's score: {player_1_score} \nPlayer 2's score: {player_2_score}")

if player_1_score > player_2_score:
    print("Player 1 wins!")
elif player_1_score < player_2_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")
