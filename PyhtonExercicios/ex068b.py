'''Crie um programa que leia o preço de vários produtos. O programa deverá perguntar se quer continuar ou não. No final,
mostre:
a) Qual é o total de gasto na compra;
b) Quantos produtos custam mais de 1000 R$;
c) Qual é o nome do produto mais barato; '''
total = totmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Valor do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de gasto na compra é: {total} R$')
print(f'Temos {totmil} produtos custando mais de 1000 R$')
print(f'O produto mais barato foi {barato} que custa {menor} R$')
