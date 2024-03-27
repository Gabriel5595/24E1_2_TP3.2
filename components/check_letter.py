def check_letter(global_guess, letter):
    if letter in global_guess:
        return False, global_guess
    else:
        global_guess.append(letter)
        return True, global_guess