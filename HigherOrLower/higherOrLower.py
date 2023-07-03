from data import data
import random
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')

print(data[0].keys())

def higher_lower():
    randomA = random.choice(data)
    randomB = random.choice(data)
    while randomA != randomB:
        randomB = random.choice(data)
    randomA_name = randomA["name"]
    randomA_follower_count = randomA["follower_count"]
    randomA_description = randomA["name"]
    randomA_country = randomA["country"]
    
    randomB_name = randomB["name"]
    randomB_follower_count = randomB["follower_count"]
    randomB_description = randomB["name"]
    randomB_country = randomB["country"]
    
    correct = 0
    correct_ans = max(randomA_follower_count, randomB_follower_count)

    print(f"Compare A: {randomA_name}, a {randomA_description}, from {randomA_country}")
    print(f"Compare A: {randomB_name}, a {randomB_description}, from {randomB_country}")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_ans == 'a' and randomA_follower_count > correct_ans:
        correct += 1
        clear()
        print(f"You're right! Current score: {correct}.")
        higher_lower()
    elif user_ans == 'b' and randomB_follower_count > correct_ans:
        correct += 1
        clear()
        print(f"You're right! Current score: {correct}.")
        higher_lower()
    else:
        clear
        print(f"Sorry. that's wrong. Final score {correct}")


higher_lower()