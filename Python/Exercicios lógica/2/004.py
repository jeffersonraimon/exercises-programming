nota1 = float(input('Coloque a nota 1: '))
nota2 = float(input('Coloque a nota 2: '))
nota3 = float(input('Coloque a nota 3: '))
nota4 = float(input('Coloque a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print('Aprovado!! ')
elif media >= 3.0 and media < 7.0:
    print('Prova final!!')
    provaFInal = float(input('Nota da prova Final: '))
    if provaFInal >= 5.0:
        print('Aprovado por conceito')
    else:
        print('Reprovado por conceito')
else:
    print('Reprovado pela média: ')