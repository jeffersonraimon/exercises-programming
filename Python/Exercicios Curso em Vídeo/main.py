"""
name = str(input('whats your name: '))
name = name.capitalize()
if name == 'Jefferson':
    print('cool name!')
else:
    print('your name is normal!')
print(f'good night, {name}!')

"""

n1 = float(input('type your first note: '))
n2 = float(input('type your second note: '))
m = (n1 + n2) / 2
print(f'your media is {m:0.2f}')
if m >= 6:
    print('nice note, man!!!')
else:
    print("that's bad =/ ")

