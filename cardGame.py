import random

def next_card(available_cards):
    return random.choice(available_cards)

def evaluate_bid(diamond_score, comp_score, user_score, comp_bid, user_bid):
    if comp_bid > user_bid:
        comp_score += diamond_score
    elif user_bid > comp_bid:
        user_score += diamond_score
    else:
        user_score += diamond_score/2
        comp_score += diamond_score/2
    return comp_score, user_score

def evaluate_winner(comp_score, user_score):
    return "You win" if user_score > comp_score else "I win"

def play_game():
    available_diamonds = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    random.shuffle(available_diamonds)
    user_available_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    comp_available_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    comp_score = 0
    user_score = 0
    while available_diamonds:
        diamond_card = available_diamonds[-1]
        diamond_score = card_values[diamond_card]
        available_diamonds.pop()
        print("Next diamond ", diamond_card)

        comp_card = next_card(comp_available_cards)
        comp_bid = card_values[comp_card]
        comp_available_cards.remove(comp_card)
        print("Your available cards", user_available_cards)

        user_card = input("Enter your bid").upper()
        user_bid = card_values[user_card]
        user_available_cards.remove(user_card)
        print("C \t U")

        print(comp_card, "\t", user_card)
        comp_score, user_score = evaluate_bid(diamond_score, comp_score, user_score, comp_bid, user_bid)
        print(comp_score, "\t", user_score)

    return evaluate_winner(comp_score, user_score)

print(play_game())





