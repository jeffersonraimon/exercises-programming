print("="*45)
print('CONVERSOR DE TEMPERATURA')

opcao = int(input('Escolha uma opção \n [1] - de ºC para ºF \n [2] - de ºF para ºC\nOpção: '))

if opcao == 1:

    tempC = float(input("Qual a temperatura em ºC: "))
    f = tempC * 9/5 + 32
    print(f'A temperatura de {tempC:0.2f}ºC é {f:0.2f}ºF')

if opcao == 2:

    tempF = float(input('Qual a temperatura em ºF: '))
    c = (tempF - 32) * 5/9
    print(f'A temperatura de {tempF:0.2f}ºF é {c:0.2f}ºC')
