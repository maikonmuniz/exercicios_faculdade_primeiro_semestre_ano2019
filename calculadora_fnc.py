## Funções
def print_menu():
    print('Calculadora')
    print('Escolha a opção abaixo:')
    print('1.....soma')
    print('2.....subtração')
    print('3.....multiplicação')
    print('4.....divisão')
    print('5.....sair')

def soma(a,b):
    return a+b

def subtrai(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def validaN2(n):
    while n == 0:
        print('Divisão por zero!')
        n = int(input('Digite n2 != 0:'))
    return n
            
def calculo(opcao):
    n1 = float(input(f'Digite o 1{chr(0xba)} número: '))
    n2 = float(input(f'Digite o 2{chr(0xba)} número: '))
    if opcao == 1:
        op='+'
        r = soma(n1,n2)
    elif opcao == 2:
        op='-'
        r = subtrai(n1,n2)
    elif opcao == 3:
        op='*'
        r = multiplica(n1,n2)
    elif opcao == 4:
        op='/'
        n2 = validaN2(n2)
        r = divide(n1,n2)
    return [r,n1,n2,op]


## Programa principal

continua = True

while continua:
    print_menu()
    opcao = int(input('Sua opção: '))
    if opcao == 5:
        continua = False
    elif opcao in [1,2,3,4]:
        r,n1,n2,op = calculo(opcao)
        print('{} {} {} = {}'.format(n1,op,n2,r))
        input('Tecle enter para continuar...')
    else:
        print('Opção inválida, digite novamente')

