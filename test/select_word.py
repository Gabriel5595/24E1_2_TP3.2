import random

def select_word(database):
    random_number = random.randint(0, 49)
    print(f"O número aleatório gerado foi {random_number}")
    
    selected_word = database[random_number]
    print(f"A palavra aleatória gerada foi {selected_word}")
    
    hidden = []
    hidden.extend(selected_word)
    print(f"A lista hidden é a seguinte: {hidden}")
    
    guess = [None] * len(hidden)
    print(f"A lista hidden é a seguinte: {guess}")
    
    return hidden, guess

def main():
    database = ["ABACAXI", "ELEFANTE", "COMPUTADOR", "GIRAFA", "ESPELHO", "CARRO", "ABAJUR", "BANANA", "GUITARRA", "XADREZ", "FOTOGRAFIA", "HIPOPOTAMO", "JANELA", "TIGRE", "UVA", "CANETA", "FUTEBOL", "PARAQUEDAS", "TURBINA", "PIANO", "MORANGO", "CACHORRO", "TECLADO", "MORCEGO", "COELHO", "CHOCOLATE", "PAPAGAIO", "DINOSSAURO", "BICICLETA", "CANECA", "MACA", "LAMPADA", "SAPO", "MONTANHA", "BARCO", "ZEBRA", "GARRAFA", "CAMISETA", "SUSHI", "NAVIO", "GAFANHOTO", "LIVRO", "SKATE", "ELETRICIDADE", "PLANETA", "FOGUETE", "VENTILADOR", "PEDRA", "VELA", "CADEIRA"]


    select_word(database)

main()