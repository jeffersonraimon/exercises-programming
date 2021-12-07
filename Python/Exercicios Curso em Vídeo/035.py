a = float(input())
b = float(input())
c = float(input())

if a < b + c and b < a + c and c < a + b:
    print('ok')
else:
    print('nope')

