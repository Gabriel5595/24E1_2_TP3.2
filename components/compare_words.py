def compare_words(hidden, guess, letter):
    correct_letter = False
    if letter.upper() in hidden:
        for i in range(len(hidden)):
            if hidden[i] == letter.upper():
                guess[i] = letter.upper()
        correct_letter = True
        return guess, correct_letter
    else:
        correct_letter = False
        return guess, correct_letter