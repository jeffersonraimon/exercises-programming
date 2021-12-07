from math import pow, sqrt, hypot

a = float(input('Coloque o valor do cateto oposto: '))
b = float(input('Coloque o valor do cateto adjacente: '))

#c = sqrt(pow(a, 2) + pow(b, 2))

c = hypot(a, b)

print(f'O valor da hipotenusa é {c:0.2f}')

