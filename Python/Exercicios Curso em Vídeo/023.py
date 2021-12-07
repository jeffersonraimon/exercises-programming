numero = int(input())

cent = numero // 100
modCent = cent % 10

dez = numero // 10
modDez = dez % 10

uni = numero // 1
modUni = uni % 10

print(modCent)
print(modDez)
print(modUni)

number = str(input('type your number: '))
print(number[0], number[1], number[2])
