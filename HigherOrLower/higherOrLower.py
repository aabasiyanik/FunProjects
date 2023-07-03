from data import data, vs_ascii
import random
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')

correct = 0
def higher_lower():
    randomA = random.choice(data)
    randomB = random.choice(data)
    while randomA == randomB:
        randomB = random.choice(data)

    randomA_name = randomA["name"]
    randomA_follower_count = randomA["follower_count"]
    randomA_description = randomA["description"]
    randomA_country = randomA["country"]
    
    randomB_name = randomB["name"]
    randomB_follower_count = randomB["follower_count"]
    randomB_description = randomB["description"]
    randomB_country = randomB["country"]
    global correct
    correct_ans = max(randomA_follower_count, randomB_follower_count)

    isValid = True
    while isValid:
        print(f"Compare A: {randomA_name}, a {randomA_description}, from {randomA_country}")
        print(vs_ascii)
        print(f"Compare B: {randomB_name}, a {randomB_description}, from {randomB_country}")
        user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_ans not in ['a', 'b']:
            clear()
            print("Invalid Input!!!")
            if correct > 0:
                print(f"Current score: {correct}\n")
        else:
            isValid = False

    if user_ans == 'a' and randomB_follower_count < correct_ans:
        correct += 1
        clear()
        print(f"You're right! Current score: {correct}.")
        higher_lower()
    elif user_ans == 'b' and randomA_follower_count < correct_ans:
        correct += 1
        clear()
        print(f"You're right! Current score: {correct}.")
        higher_lower()
    else:
        clear()
        print(f"Sorry. that's wrong. Final score {correct}")

higher_lower()