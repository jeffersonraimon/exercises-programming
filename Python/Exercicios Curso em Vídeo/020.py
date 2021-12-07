from random import shuffle

nome1 = str(input('informe o primeiro nome: '))
nome2 = str(input('informe o segundo nome: '))
nome3 = str(input('informe o terceiro nome: '))
nome4 = str(input('informe o quarto nome: '))

lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print(lista)
