from components.check_guesses import check_guesses
from components.check_letter import check_letter
from components.select_word import select_word
from components.compare_words import compare_words
from components.draw_hangman import draw_hangman

def main():
    if __name__ == "__main__":
        database = ["ABACAXI", "ELEFANTE", "COMPUTADOR", "GIRAFA", "ESPELHO", "CARRO", "ABAJUR", "BANANA", "GUITARRA", "XADREZ", "FOTOGRAFIA", "HIPOPOTAMO", "JANELA", "TIGRE", "UVA", "CANETA", "FUTEBOL", "PARAQUEDAS", "TURBINA", "PIANO", "MORANGO", "CACHORRO", "TECLADO", "MORCEGO", "COELHO", "CHOCOLATE", "PAPAGAIO", "DINOSSAURO", "BICICLETA", "CANECA", "MACA", "LAMPADA", "SAPO", "MONTANHA", "BARCO", "ZEBRA", "GARRAFA", "CAMISETA", "SUSHI", "NAVIO", "GAFANHOTO", "LIVRO", "SKATE", "ELETRICIDADE", "PLANETA", "FOGUETE", "VENTILADOR", "PEDRA", "VELA", "CADEIRA"]
        
        hidden, guess = select_word(database)
        global_guess = []
        errors = 0
        while errors <= 5:
            print(hidden)
            print(guess)
            print(global_guess)
            print("\n")
            
            letter = input("Please guess a letter: ")
            
            if check_letter(global_guess, letter):
                guess, correct_letter = compare_words(hidden, guess, letter)
                
                if correct_letter:
                    print(f"Correct! Letter '{letter}' is present in the word!\n")
                    
                    if check_guesses(guess):
                        print("You win!")
                        print(hidden)
                        break
                    else:
                        pass
                    
                else:
                    errors += 1
                    draw_hangman(errors)
            
            else:
                print("This letter has already been selected. Please select another.\n")


main()