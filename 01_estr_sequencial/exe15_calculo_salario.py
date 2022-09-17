# Crie um programa que pergunte ao usuário quanto ele ganha por
# hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do salário no referido mês, sabendo que
# serão descontados 11% para o Imposto de Renda, 8% para o INSS e 
# 5% para o sindicato. O programa deve exibir:
#
# a. salário bruto
# b. quanto pagou ao INSS
# c. quanto pagou ao sindicato
# d. o salário líquido
# e. exiba as informações numa tabela bem organizada.

val_hora = float(input('Quanto você ganha por hora trabalhada? R$'))
tot_hora = int(input('Quantas hora você trabalhou neste mês: '))
bruto = tot_hora * val_hora
imp_renda = (bruto * 11) / 100
inss = (bruto * 8) / 100
sindicato = (bruto * 5) / 100
liquido = bruto - (imp_renda + inss + sindicato)
print()

print('-' * 30)
print(f'+ Salário Bruto : R${bruto:.2f}\n'
      f'─ IR (11%) : R${imp_renda:.2f}\n'
      f'─ INSS (8%) : R${inss:.2f}\n'
      f'─ Sindicato (5%) R$ : R${sindicato:.2f}\n'
      f'= Salário Líquido : R${liquido:.2f}')
print()
