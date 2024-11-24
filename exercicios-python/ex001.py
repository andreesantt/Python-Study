#Calcular média aluno
nota1 = float(input('Primeira nota: '))
#Aluno digita primeira nota
nota2 = float(input('Segunda nota: '))
#Aluno digita segunda nota
media = (nota1 + nota2) / 2
#Soma primeira nota com a segunda e divide por dois e encontra média
if media >= 6:
    print('Parabéns, sua média foi {}.'.format(media))
    print('Você foi \033[4;;42mAPROVADO\033[;m')
elif media == 5.5:
    print('Ops!!! Sua média foi {}'.format(media))
    print('Você está de \033[4;;44mRECUPERAÇÃO\033[;m')
else:
    print('Essa não! Sua nota foi {}'.format(media))
    print('Você foi \033[4;;41mREPROVADO\033[;m')
    