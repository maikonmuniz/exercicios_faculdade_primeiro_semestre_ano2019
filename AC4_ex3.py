
# recebe n
n=int(input())
# enquanto n for menor ou igual a zero, ele é inválido, então pede n novamente,
# e o laço finaliza quando n > 0
while n<=0:
    print('Número inválido!')
    n=int(input())
print('Número aceito!')

# A variável contadora deve percorrer todos os números de 1 a N (inclusive)
# portanto começa em 1 e o while executa enquanto x for menor ou igual a N

x=1
soma=0
while x<=n:
    soma+=x     # Incrementa o valor de cada x na variável soma
    x+=1        # Vai pro próximo x. Essa em geral é a última instrução do while.
print(soma)
