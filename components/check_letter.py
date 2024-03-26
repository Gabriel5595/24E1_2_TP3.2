def check_letter(global_guess, letter):
    if letter.upper() in global_guess:
        return True
    else:
        return False