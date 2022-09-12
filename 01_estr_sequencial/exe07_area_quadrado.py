# Calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = int(input('Digite o comprimento de um dos lados do quadrado: '))
area = lado ** 2

print(f'O dobro da área de um quadrado com lados de {lado}cm é igual a {(area * 2):.1f}cm².')
