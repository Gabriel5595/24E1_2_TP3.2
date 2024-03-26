import random

def select_word(database):
    random_number = random.randint(0, 49)
    
    selected_word = database[random_number]
    
    hidden = []
    hidden.extend(selected_word)
    
    guess = [None] * len(hidden)
    
    return hidden, guess