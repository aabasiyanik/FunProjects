import random
from os import system, name
def clear():
   if name == 'nt':
      _ = system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    draw = random.choice(cards)

    return draw

def blackjack():
    isValid = True
    while isValid:
        play_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_or_no.lower() not in ['y', 'n']:
            print("Please type 'y' or 'n'\n")
        else:
            isValid = False

    if play_or_no.lower() == 'y':
        clear()
        pass
    else:
        exit()

    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]

    if sum(user) == 21 and sum(computer) < 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win with Blackjack")
        blackjack()

    is2 = True
    while is2:
        ansValid = True
        while ansValid:
            print(f"\tYour cards: {user}, current score: {sum(user)}")
            print(f"\tComputer's first card: {computer[0]}")
            ans = input("Type 'y' to get another card, type 'n' to pass: ")
            if ans.lower() not in ['y', 'n']:
                print("Please type 'y' or 'n'\n")
            else:
                ansValid = False

        if ans.lower() == 'y':
            user.append(draw_card())
            if sum(user) == 21:
                print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win with Blackjack")
                blackjack()
            elif sum(user) > 21:
                if 11 in user and sum(user) > 21:
                    aces = user.count(11)
                    while aces > 0 and sum(user) > 21:
                        user[user.index(11)] = 1
                        aces -= 1
                if sum(user) > 21:
                    print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou went over. You lose.")
                    blackjack()
                else:
                    pass
            else:
                pass
        else:
            is2 = False
    
    while sum(computer) < 17:
        computer.append(draw_card())
    
        if 11 in computer and sum(computer) >= 17 and sum(computer) > 21:
            aces = computer.count(11)
            while aces > 0 and sum(computer) > 21:
                computer[computer.index(11)] = 1
                aces -= 1

    if sum(computer) > 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win")
        blackjack()
    elif sum(computer) == 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nComputer Win with Blackjack")
        blackjack()
    elif sum(computer) > sum(user):
        print(print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Lose"))
        blackjack()
    elif sum(computer) < sum(user):
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win")
        blackjack()
    elif sum(computer) == sum(user):
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nDraw")
        blackjack()


blackjack()