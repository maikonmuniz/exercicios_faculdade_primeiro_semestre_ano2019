''' Estas são as senhas salvas no sistema,
o seu código deve comparar as senhas
digitadas com as senhas abaixo para efetuar
o login dos usuários.
Não apague este trecho do cógido.
'''
usuario_1 = 'Bettina'
senha_1 = 'MeUpRiMeIrOmILhAo'

usuario_2 = 'Kauã'
senha_2 = 'treisconchada'

usuario_3 = 'Jenifer'
senha_3 = 'tinder123'

# começe o seu código a partir daqui:

# Passo 1 - Validar o usuário
flag_usuario = False
while not flag_usuario:
    usuario = input()
    if usuario == usuario_1 or usuario == usuario_2 or usuario == usuario_3:
        flag_usuario = True
        print('Olá, {}!'.format(usuario))
    else:
        print('Usuário desconhecido, tente novamente!')

# Passo 2 - Descobrir qual usuário está fazendo login
#           e salvar a senha dele para verificação
if usuario == usuario_1:
    senha_chave = senha_1
elif usuario == usuario_2:
    senha_chave = senha_2
else:
    senha_chave = senha_3

# Passo 3 - Validar a senha do usuário em questão
flag_senha = False
flag_bloqueia = False
tentativas = 1
while not (flag_senha or flag_bloqueia):
    senha = input()
    if senha == senha_chave:
        flag_senha = True
        print('Bem vindo(a) ao nosso portal online!')
    elif tentativas < 5:  
        print('Senha incorreta, tente novamente!')  
    else:
        flag_bloqueia = True
        print('Usuário bloqueado, entre em contato por telefone para desbloquear a sua conta!')
    tentativas += 1

# Funcionamento do bloco if para validação da senha:
    # Se a senha estiver correta (if), a flag da senha é True
    # --> termina o laço com a mensagem de boas vindas.

    # Se a senha estiver errada (elif) e o número de tentativas
    # for menor que 5, permite uma nova tentativa.

    # Se o número de tentativas for 5 (else), a flag de bloqueio é True
    # --> termina o laço com a mensagem de bloqueio
