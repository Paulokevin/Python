'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual é o valor do sslário do funcionário? '))
if salario > 1250:
    novosal = salario + salario*0.1
else:
    novosal = salario + salario*0.15
print('O antigo salário do funcionário era {} e agora passa a ser {}'.format(salario, novosal))
