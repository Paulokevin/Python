'''Escreva um programa que leia dois números inteiros e compare-os, monstrando na tela uma mensagem:
-O primeiro valor é maior; -O segundo valor é maior; -não existe valor maior, os dois são iguais'''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Entre {} e {} não existe maior ou menor, pois ambos são iguais'.format(num1, num2))