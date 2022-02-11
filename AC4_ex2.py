n1=int(input())
n2=int(input())

# Se o primeiro número for maior, trocar os dois números de lugar.
if n1>n2: 
  n1,n2=n2,n1 # Iremos aprender como fazer essa troca na próxima aula.
              # mas bastaria fazer a troca com o uso de uma variável auxiliar.
              # aux = n1
              # n1 = n2
              # n2 = aux
              # Outra solução seria utilizar duas novas variáveis para guardar
              # o maior e o menor número:
              # if n1>n2:
              #     maior = n1
              #     menor = n2
              # else:
              #     maior = n2
              #     menor = n1
              # E então fazer o resto do programa com as variáveis maior e menor   

print('O menor número é {} e o maior é {}!'.format(n1,n2))
print('Os pares entre {} e {} são:'.format(n1,n2))

# Se o menor número for par, inicializa x = menor, senão x = menor+1
if n1%2==0:
  x=n1
else:
  x=n1+1

# Percorre os números de x até n2 (inclusive) pulando de 2 em 2.
while x<=n2:
  print(x)
  x+=2
