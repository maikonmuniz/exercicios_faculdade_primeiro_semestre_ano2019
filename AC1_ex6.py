import math

area = int(input('Digite a área a ser pintada:'))

# Constantes
m2_por_litro = 5
litros_lata = 18
litros_galao = 3.6
preco_lata = 85.
preco_galao = 23.

# Quantidade de tinta necessária
litros = area/m2_por_litro

############### Item a) ###############

# Quantidade de latas de 18l
N_latas = math.ceil(litros/litros_lata)
custo_a = N_latas*preco_lata

# Impressão do resultado
print('a) Latas de 18l: {} Custo: R$ {:.2f}'
      .format(N_latas,custo_a))

############### Item b) ###############

# Quantidade de latas de 3.6l
N_galoes = math.ceil(litros/litros_galao)
custo_b = N_galoes*preco_galao

# Impressão do resultado
print('b) Latas de 3.6l: {} Custo: R$ {:.2f}'
      .format(N_galoes,custo_b))

############### Item c) ###############

# Quantidade de latas de 3.6l
N_latas_c = int(litros//litros_lata)
# A divisão truncada arredonda para baixo o valor, então 
# a parte decimal vai ser a parte da tinta que devemos comprar
# em latas de 3.6l, ou seja, o resto da divisão acima.
litros_faltando = litros%litros_lata
N_galoes_c = math.ceil(litros_faltando/litros_galao)
custo_c = N_latas_c*preco_lata + N_galoes_c*preco_galao

# Impressão do resultado
print('c) Latas de 18l: {} Latas de 3.6l: {} Custo: R$ {:.2f}'
      .format(N_latas_c,N_galoes_c,custo_c))
