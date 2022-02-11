valor = float(input())

# Cálculo da quantidade de cada nota
nota100 = int(valor//100)
valor = valor%100
nota50 = int(valor//50)
valor = valor%50
nota20 = int(valor//20)
valor = valor%20
nota10 = int(valor//10)
valor = valor%10
nota5 = int(valor//5)
valor = valor%5
nota2 = int(valor//2)
valor = valor%2

# Cálculo da quantidade de cada moeda
moeda100 = int(valor//1)
valor = valor%1
moeda50 = int(valor//0.5)
valor = round(valor%0.5,2)
moeda25 = int(valor//0.25)
valor = round(valor%0.25,2)
moeda10 = int(valor//0.1)
valor = round(valor%0.1,2)
moeda5 = int(valor//0.05)
valor = round(valor%0.05,2)
moeda1 = int(valor//0.01)


# Impressão caso a quantidade seja diferente de 0
if nota100 != 0:
  print('{} nota(s) de R$ 100.00'.format(nota100))
if nota50 != 0:
  print('{} nota(s) de R$ 50.00'.format(nota50))
if nota20 != 0:
  print('{} nota(s) de R$ 20.00'.format(nota20))
if nota10 != 0:
  print('{} nota(s) de R$ 10.00'.format(nota10))
if nota5 != 0:
  print('{} nota(s) de R$ 5.00'.format(nota5))
if nota2 != 0:
  print('{} nota(s) de R$ 2.00'.format(nota2))
if moeda100 != 0:
  print('{} moeda(s) de R$ 1.00'.format(moeda100))
if moeda50 != 0:
  print('{} moeda(s) de R$ 0.50'.format(moeda50))
if moeda25 != 0:
  print('{} moeda(s) de R$ 0.25'.format(moeda25))
if moeda10 != 0:
  print('{} moeda(s) de R$ 0.10'.format(moeda10))
if moeda5 != 0:
  print('{} moeda(s) de R$ 0.05'.format(moeda5))
if moeda1 != 0:
  print('{} moeda(s) de R$ 0.01'.format(moeda1))
