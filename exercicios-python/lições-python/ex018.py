import math
angulo = float(input('Digite um ângulo '))
sen = math.sin((math.radians(angulo)))
cos = math.cos((math.radians(angulo)))
tg = math.tan((math.radians(angulo)))
print('O seno de {}° vale {:.2f}'.format(angulo, sen))
print('O conseno de {}° vale {:.2f}'.format(angulo, cos))
print('A tangente de {}° vale {:.2f}'.format(angulo, tg))