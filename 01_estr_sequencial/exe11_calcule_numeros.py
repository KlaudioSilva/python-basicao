# Faça um programa que peça dois números inteiros e um real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo
# b. a soma do triplo do primeiro com o terceiro
# c. o terceiro elevado ao cubo.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
n3 = float(input('Digite um número real: '))

trip = n1 * 3
print(f'O produto do dobro de {n1} com metade {n2} é igual a {n3}')
print(f'O triplo de {n1} é {trip} somado com {n3} temos {(trip + n3)}')
print(f'{n3} elevado ao cubo é {(n3 ** 3):.2f}')
print()