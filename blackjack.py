import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    number = random.randint(0, 12)
    card = cards[number]
    return card

def show2(a, b):
    total = a + b
    print(f"Your first card is {a}, your second card is  {b}.")
    print(f"Your current total is {total}")


def play():
    card1 = deal_cards()
    card2 = deal_cards()
    show2(card1, card2)
    print("do you want another card? y/n")
    choice = input()
    if choice == 'y':
        card3 = deal_cards()
        total3 = card1 + card2 + card3
        print(card1, card2, card3, total3)
    if total3 > 21 or total3 < 17:
        print("You lose")
    elif total3 >= 17 or total3 <= 20:
        print("you win")


def start():
    print("Welcome, do you want to play blackjack? y/n")
    choice1 = input()
    if choice1 == 'y':
        play()
    elif choice1 == 'n':
        print("See you next time!")
    else:
        print("Thats not right.")

start()