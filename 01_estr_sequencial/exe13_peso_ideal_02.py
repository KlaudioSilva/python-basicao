# Tendo como dado de entrada a altura (h) de uma pessoa, construa
# um algoritmo que calcule seu peso ideal, para homens e para mulheres.
h = float(input('Qual é a sua altura: '))
s = str(input('Qual é o seu sexo [M/F]: '))

if (s == 'M') or (s == 'm'):
    peso = (72.7 * h) - 58
    print(f'Sendo do sexo masculino e com a altura de {h}mt, seu peso ideal é de {peso:.2f}kg.')
elif (s == 'F') or (s == 'f'):
    peso = (62.1 * h) - 44.7
    print(f'Sendo do sexo feminino e com a altura de {h}mt, seu peso ideal é de {peso:.2f}kg.')
print()
