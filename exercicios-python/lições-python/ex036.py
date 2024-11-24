#Programa de aprovação de empréstimo bancário para compra de uma casa;
#Valor do imóvel;
#Salário do titular;
#Quantos anos de parcelas;
imovel = float(input('Valor do imóvel: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos irá parcelar? '))
meses = anos * 12 #Transformando anos em meses para descobrir valor parcela
parcelas = imovel / meses #Divisão para encontrar valor parcela
cond = (30 *  salario) / 100 #Condição de 30% do salário
if parcelas > cond:
    print('Desculpe, você não tem condições necessárias')
else:
    print('Parebéns, você irá financiar este imóvel!!!')
    print('As parcelas mensais durante {} anos será de R${:.2f}'.format(anos, parcelas))