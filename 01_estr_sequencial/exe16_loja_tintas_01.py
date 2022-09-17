# Crie um programa para uma loja de tintas. O programa deverá pedir
# o tamanho em metros quadrados da área a ser pintada. Considere que 
# a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe
# ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

area = float(input('Qual é o tamanho da área a ser pintada [m²]: '))
litros = area / 3
latas = litros / 18
tot_preco = latas * 80

print(f'Para cobrir uma área de {area}m², serão necessários {litros:.1f} litros de tinta.\n'
      f'Necessitando então de {latas:.1f} latas de 18 litros.\n'
      f'Com o preço de R$80,00 por lata o total gasto será de R${tot_preco:.2f}.')
print()
