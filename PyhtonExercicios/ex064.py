'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final mostre quantos números foram  digitados e qual foi a soma entre eles
(Desconsiderando a Flag)'''
cont = soma = 0
while True:
    num = int(input('Digite um valor [Digite 999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi de {soma}!')