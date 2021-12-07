from random import choice

nome1 = input('primeiro nome: ')
nome2 = input('segundo nome: ')
nome3 = input('terceiro nome: ')
nome4 = input('quarto nome: ')

escolhido = [nome1, nome2, nome3, nome4]

print(f'o escolhido é: {choice(escolhido)}')


