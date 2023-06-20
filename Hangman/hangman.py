import random
from ascii import stages

chances = 6

word_list = ["elephant", "banana", "sunflower", "giraffe", "piano", "chocolate", "mountain", "umbrella", "watermelon", "butterfly", "sapphire", "pineapple", "dragonfly", "peacock", "moonlight", "cappuccino", "whisper", "jigsaw", "velvet", "tornado"]
choosen_word = random.choice(word_list)
word = ["_"] * len(choosen_word)
end = False

while not end:
    print(f"{' '.join(word)}")
    print("---------")
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print(f"You've already guessed {guess}")
    for index in range(len(choosen_word)):
        letter = choosen_word[index]
        if guess == letter:
            word[index] = guess
        elif guess not in choosen_word:
            print(stages[chances])
            print(f"You guessed {guess}, which is not in the word. You lose a life")
            chances -= 1
            break
    if "_" not in word:
        print("You won")
        end = True
    elif chances < 0:
        print("You lost")
        end = True