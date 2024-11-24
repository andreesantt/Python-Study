#Digitar duas notas e calcular média p/ saber se está aprovado ou não
print('Para saber se você se você passou de ano digite: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
m = (nota1 + nota2) / 2
from time import sleep
print('Calculando média...')
sleep(3)
if m < 5.0:
    print('Que pena, sua média foi de {}\n você foi \033[4;;41mREPROVADO\033[;m'.format(m))
elif m == 5.0 or m == 6.9:
    print('Sua média foi de {}\nE você está de \033[4;;46mRECUPERAÇÃO\033[;m'.format(m))
else:
    print('Muito bem, sua média foi de {}\nVocê está \033[4;;42mAPROVADO\033[;m '.format(m))