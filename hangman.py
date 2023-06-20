import random
word_list = ["elephant", "banana", "sunflower", "giraffe", "piano", "chocolate", "mountain", "umbrella", "watermelon", "butterfly", "sapphire", "pineapple", "dragonfly", "peacock", "moonlight", "cappuccino", "whisper", "jigsaw", "velvet", "tornado"]
choosen_word = random.choice(word_list)
print(choosen_word)
guess = input("Guess a letter: ").lower()
word = ["_"] * len(choosen_word)

for index in range(len(choosen_word)):
    letter = choosen_word[index]
    if guess == letter:
        word[index] = guess

print(word)