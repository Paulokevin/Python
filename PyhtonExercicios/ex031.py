'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Insiria um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
#Definindo o maior:
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
     maior = n3
#Definindo o menor:
if n1 <= n2 and n1 <= n3:
     menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
print('O maior número é o {}'.format(maior))
print('O menor número é o menor {}'.format(menor))
