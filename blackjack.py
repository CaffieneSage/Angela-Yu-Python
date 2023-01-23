import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    number = random.randint(0, 12)
    card = cards[number]
    return card

card1 = deal_cards()
card2 = deal_cards()
total = card1 + card2
print(card1)
print(card2)
print(f"The total is: {total}")
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
elif choice == 'n':
    total2 = card1 + card2
    print(card1, card2, total2)
    if total2 < 17:
        print("You loose.")
    elif total2 > 21:
        print("You loose.")
    elif total2 >= 17 or total2 <= 21:
        print("You win!")
else:
    print("invalid input")