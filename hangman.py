import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chances = 6

word_list = ["elephant", "banana", "sunflower", "giraffe", "piano", "chocolate", "mountain", "umbrella", "watermelon", "butterfly", "sapphire", "pineapple", "dragonfly", "peacock", "moonlight", "cappuccino", "whisper", "jigsaw", "velvet", "tornado"]
choosen_word = random.choice(word_list)
print(choosen_word)
word = ["_"] * len(choosen_word)
end = False

while not end:
    guess = input("Guess a letter: ").lower()
    for index in range(len(choosen_word)):
        letter = choosen_word[index]
        if guess == letter:
            word[index] = guess
        else:
            pass
    if "_" not in word:
        print("You win")
        end = True
    elif chances == 0:
        print("You lost")

print(word)