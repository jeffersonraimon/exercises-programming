ladoA = float(input('Informe o Lado A: '))
ladoB = float(input('Informe o Lado B: '))
ladoC = float(input('Informe o Lado C: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and (ladoC < (ladoA + ladoB)):
  
    print('É triangulo!')  

    if ladoA == ladoB and ladoA == ladoC:
        print('Triangulo equilatero: ')
    if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('Triangulo isosceles: ')
    else:
        print('Triangulo Escaleno! ')
else:
    print('Não forma triangulo')