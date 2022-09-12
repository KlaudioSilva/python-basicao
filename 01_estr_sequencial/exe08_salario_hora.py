# crie um programa que pergunte quanto o usuário ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o salário no referido mês.
val_hora = float(input('Quanto você ganha por hora R$'))
tot_hora = int(input('Quantas horas você trabalha por mês: '))

salario = val_hora * tot_hora

print(f'Ganhando R${val_hora} por hora e trabalhando {tot_hora} horas no mês, o seu salário será R${salario:.2f}.')
