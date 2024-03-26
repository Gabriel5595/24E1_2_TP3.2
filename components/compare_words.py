def compare_words(hidden, guess, letter):
    if letter.upper() in hidden:
        for i in range(len(hidden)):
            if hidden[i] == letter.upper():
                guess[i] = letter.upper()
        return guess, True
    else:
        return guess, False