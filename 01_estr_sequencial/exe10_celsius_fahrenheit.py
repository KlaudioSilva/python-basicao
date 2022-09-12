# Converta a temperatura de graus Celsius para graus Fahrenheit.
cel = float(input('Qual é a temperatura em graus celsius [C°]: '))
fah = ((cel * 9) / 5) + 32

print(f'A temperatura de {cel}°C, convertida para graus fahrenheit é {fah:.1f}°F.')
