'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
num = int(input('Insira o valor que você queira fazer a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, c*1))