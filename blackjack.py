import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    draw = random.choice(cards)

    return draw

def blackjack():
    play_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_or_no == 'y':
        pass
    else:
        exit()

    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]

    if sum(user) == 21 and sum(computer) < 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYour went over. You Win")
        blackjack()

    is2 = True
    while is2:
        print(f"\tYour cards: {user}, current score: {sum(user)}")
        print(f"\tComputer's first card: {computer[0]}")
        ans = input("Type 'y' to get another card, type 'n' to pass: ")
        if ans == 'y':
            user.append(draw_card())
            if sum(user) > 21:
                print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYour went over. You lose")
                blackjack()
            elif sum(user) == 21:
                print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win with Blackjack")
            else:
                pass
        else:
            is2 = False
    
    while sum(computer) < 17:
        computer.append(draw_card())
    
    if sum(computer) > 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\nYou Win")
        blackjack()
    elif sum(computer) == 21:
        print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}\Computer Win with Blackjack")
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