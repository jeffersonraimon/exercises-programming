import math

angulo = float(input('Informe o angulo: '))

cos = math.cos(math.radians(angulo))
sen = math.sin((math.radians(angulo)))
tan = math.tan(math.radians(angulo))



print(f'o cosseno é: {cos:0.2f} o seno é {sen:0.2f} e a tangente é {tan:0.2f}')
