def check_guesses(guess):
    if None in guess:
        return False
    else:
        return True

def main():
    guess = ['E', 'L', 'E', 'T', 'R', 'I', 'C', 'I', 'D', 'A', 'D', 'E']
    
    check_guesses(guess)

main()