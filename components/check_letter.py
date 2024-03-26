def check_letter(global_guess, letter):
    if letter.upper() in global_guess:
        return False
    else:
        return True