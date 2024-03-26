def check_letter(global_guess, letter):
    if letter.upper() in global_guess:
        return True
    else:
        return False

def main():
    global_guess = ['D', 'E', 'R']
    check_letter(global_guess, 'g')

main()