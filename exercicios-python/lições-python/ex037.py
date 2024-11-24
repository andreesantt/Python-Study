#Digite um número qualquer e escolha a base de conversão;
#Binário, octal, hexadecimal.
n = int(input("Digite um número inteiro: ")) #Usuário digita um número inteiro
print('Converter {} para:\n\033[7;30;47m1 - Binário:\033[;m\n\033[7;30;41m2 - Octal:\033[;m\n\033[7;30;44m3 - Hexadecimal:\033[;m'.format(n))
bc = int(input('Escolha a base de conversão: ')) #Usuário escolhe uma das opções dada acima de conversão
from time import sleep
print("\033[4;30;47mPROCESSANDO...\033[;m")
sleep(5)
if bc == 1:
    print('Você escolheu a opção de número {}'.format(bc))
    binario = bin(n) #Faz conversão da variável N de um número inteiro para um número binário
    print('Portanto seu número binário é: {}'.format(binario))
elif bc == 2:
    print('Você escolheu o {}'.format(bc))
    octal = oct(n) #Faz conversão da variável N de um número inteiro para um número octal
    print('Portanto seu número octal é {}'.format(octal))
elif bc == 3:
    print('Você escolheu a opção de número {}'.format(bc))
    hexadecimal = hex(n) #Faz conversão da variável N de um número inteiro para um número hexadecimal
    print('Portanto seu número hexadecimal vale {}'.format(hexadecimal))
else:
    print(('Desculpe, tente novamente ;-;'))