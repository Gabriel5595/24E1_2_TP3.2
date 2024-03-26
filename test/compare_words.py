def compare_words(hidden, guess, letter):
    if letter.upper() in hidden:
        for i in range(len(hidden)):
            if hidden[i] == letter.upper():
                guess[i] = letter.upper()
        print(f"Nova lista guess: {guess}")
        return guess, True
    else:
        return guess, False


def main():
    hidden = ['E', 'L', 'E', 'T', 'R', 'I', 'C', 'I', 'D', 'A', 'D', 'E']
    guess = [None, None, None, None, None, None, None, None, None, None, None, None]
    
    compare_words(hidden, guess, "e")

main()