wages = float(input())

if wages > 1250:
    up = wages * (10/100)
else:
    up = wages * (15/100)

print(up+wages)