distance = float(input('distance of travel [KM]: '))
if distance <= 200.0:
    price = 0.50 * distance
else:
    price = 0.45 * distance
print(f'price of ticket is U$ {price}')
