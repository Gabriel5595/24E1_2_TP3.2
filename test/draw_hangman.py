def draw_hangman(errors):
    if errors == 1:
        print("""
    0

You have 1 error so far.
""")
    elif errors == 2:
        print("""
    0
   /

You have 2 error so far.
""")
    elif errors == 3:
        print("""
    0
   /|

You have 3 error so far.
""")
    elif errors == 4:
        print("""
    0
   /|\\

You have 4 error so far.
""")
    elif errors == 5:
        print("""
    0
   /|\\
   /

You have 5 error so far.
""")
    elif errors == 6:
        print("""
    0
   /|\\
   / \\

You have 6 error so far. Game over!
""")

def main():
    draw_hangman(5)

main()