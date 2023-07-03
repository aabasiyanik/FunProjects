from data import data
import random

print(data[0])

def higher_lower():
    randomA = random.choice(data)
    randomB = random.choice(data)
    while randomA != randomB:
        randomB = random.choice(data)
    
    

higher_lower()