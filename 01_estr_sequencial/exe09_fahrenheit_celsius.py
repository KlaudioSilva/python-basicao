# Converta a temperatura de graus Fahrenheit para graus Celsius.
fah = float(input('Qual é a temperatura em graus fahrenheit [°F]: '))
cel = ((fah - 32) * 5) / 9

print(f'A temperatura de {fah}°F, convertida para graus celsius é {cel:.1f}°C.')
