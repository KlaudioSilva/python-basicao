"""
Um pescador quer controlar o rendimento diário de seu trabalho. Toda vez
que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de SP (50kg) deve pagar uma multa de R$4.00 por quilo
excedente. Crie um programa que leia a variável 'peso' e calcule o excesso.
Grave na variável 'excesso' a quantidade de quilos além do limite e na
variável 'multa' o valor da multa que o pescador deve pagar. Mostre as
mensagens adequadamente.
"""

peso = int(input('Quantos quilos de peixe você pescou? [kg]: '))
excesso = peso - 50

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Você excedeu a limite de peso diário em {excesso}kg.\n'
          f'Com uma multa de R$4,00 por quilo excedido você vai\n'
          f'pagar uma multa total de R${multa:.2f}.')
else:
    print(f'Hoje você pescou {peso}kg de peixes. Este peso está\n'
          f'dentro do limite diário de 50kg..')
print()
