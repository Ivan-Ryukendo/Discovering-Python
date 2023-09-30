import random

with open('E:\Mine\Learning\Coding\Discovering Python\Projects\Random word Gen\words.txt', 'r') as file:
    words = file.read().splitlines()

random_index = random.randint(0, len(words) - 1)

random_word = words[random_index]

print("Randomly selceted word: ", random_word)