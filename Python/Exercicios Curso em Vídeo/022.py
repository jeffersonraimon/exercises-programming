fullname = str(input('Type your full name, please: ')).strip()
print(f'Your name in upper is {fullname.upper()}')
print(f' Your name in lower is {fullname.lower()}')
nospace = fullname.replace(' ', '')
print(f' Your name has {nospace} letters')
firstname = fullname.split()
print(f'Your first name is {firstname} and has {len(firstname[0])} letters')

