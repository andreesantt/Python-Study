#Ler ano de nascimento de um jovem e informe se está ou não no periodo de alistamento militar
print('Para saber se você está para se alistar digite: ')
ano = int(input('Seu ano de nascimento: '))
from datetime import date
idade = date.today().year - ano
if idade == 18:
    print('Você tem {} anos e precisa se alistar !!!'.format(idade))
elif idade < 18:
    print('Você tem {} anos, ainda é menor de idade\nnão se preocupe com isso agora!!!'.format(idade))
    resta = 18 - idade
    print('Resta {} anos para você se alistar'.format(resta))
else:
    print('Seu período de alistamento já passou, você tem {} anos\nProcure a Junta Militar da sua cidade!!!'.format(idade))
    venceu = idade - 18
    print('Já se passaram {} anos desde que você deveria ter se alistado'.format(venceu))
