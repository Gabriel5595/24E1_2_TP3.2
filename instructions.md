# Instructions

7. Crie uma lista contendo nomes diversos, em diversas categorias, tais como frutas, carros, objetos, entre outros.

8. Crie uma função que receba como parâmetro o vetor de nomes, de onde deverá ser escolhida aleatoriamente uma palavra. O retorno da função deve ser uma lista contendo os caracteres da palavra selecionada.

9. Crie uma função que receba como parâmetro uma lista contendo a palavra a ser adivinhada (hidden), como retornada na questão 8, uma segunda lista, que conterá a palavra formada com os caracteres adivinhados pelo jogador (guess) e o caracter que foi sugerido pelo usuário. A função deve verificar a existência do caracter dentro da lista hidden e preencher a lista guess com o caracter sugerido, na posição correta, caso ele esteja contido na palavra. O retorno deve ser a lista guess, contendo as letras já adivinhas e um valor booleano, que indicará a existência da letra na palavra. O protótipo da função pode seguir o seguinte modelo:

        def checa_letra(hidden, guess, letter)

        return guess, is_letter

10. Crie uma função que verifique se todas as posições da lista usada para receber as letras sugeridas pelo usuário já foram preenchidas. Como sugestão, a lista de sugestões pode ser preenchida com o valor None em todas as posições, devendo ter o mesmo tamanho da palavra que será adivinhada.

11. Crie uma função para desenhar o enforcado, à medida que letras erradas são escolhidas. O limite será de 6 erros e a seguinte lista de caracteres poderá ser usada: ["0", "/", "|", "\\", "/", " \\"].

12. Crie uma função que controle quais letras do alfabeto já foram escolhidas, e impeça que letras repetidas sejam contadas.

13. Crie um fluxograma que descreva a estrutura do jogo.

14. Com base no fluxograma da questão 7, crie a estrutura completa do jogo, utilizando as funções desenvolvidas ao longo da atividade, bem como criando as variáveis que serão utilizadas para controlar as ações do jogo.

15. Realize o teste do código desenvolvido, apresentando o resultado para cinco rodadas do jogo.