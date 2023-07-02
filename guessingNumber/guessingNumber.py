import random

def guessing_num():
    isValid = True
    while isValid:
        difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
        if difficulty not in ['hard', 'easy']:
            print("Wrong input")
        else:
            isValid = False

    if difficulty == 'hard':
        attempts = 5
        print(f"You have {attempts} remaning to guess the number.")
    else:
        attempts = 10
        print(f"You have {attempts} remaning to guess the number.")

    choosen_num = random.randint(1,100)
    user_ans = 0
    while attempts > 0 or user_ans == choosen_num:
        user_ans = int(input("Make a guess: "))
        if user_ans == choosen_num:
            return (f"You got it the answer was {user_ans}")
        elif user_ans != choosen_num:
            attempts -= 1
            if attempts < 1 and user_ans < choosen_num:
                return "Too low\nYou've run out of guesses, you lose"
            elif attempts < 1 and user_ans > choosen_num:
                return "Too high\nYou've run out of guesses, you lose"
        
        if user_ans < choosen_num:
            print(f"Too low.\nGuess Again\nYou have {attempts} attempts remaining to the guess number.")
        elif user_ans > choosen_num:
            print(f"Too high.\nGuess Again\nYou have {attempts} attempts remaining to the guess number.")

print(guessing_num())