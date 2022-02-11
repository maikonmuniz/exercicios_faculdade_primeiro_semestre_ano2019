lado = float(input('Digite o comprimento do lado do hexágono:'))

area_triangulo = lado**2 * 3**(1/2) / 4
area_hexagono = 6*area_triangulo
print('A área do hexágono é:',area_hexagono)
