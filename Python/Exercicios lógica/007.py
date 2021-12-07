#question7
hourP = float(input())
hourW = float(input())
wagesBrute = hourP * hourP
lion = wagesBrute * (11/100)
inss = wagesBrute * (8/100)
sindicate = wagesBrute * (5/100)
wagesLiquid = wagesBrute - (lion + inss + sindicate)
print(wagesBrute)
print(lion)
print(inss)
print(sindicate)
print(wagesLiquid)