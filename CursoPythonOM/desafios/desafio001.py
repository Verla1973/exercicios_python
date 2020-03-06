usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite sua senha: ')

usuario_bd = 'Verlã'
senha_bd = '180317'

if usuario_bd == usuario and senha_bd == senha:
    print(f'Bem vindo {usuario},você está logado no sistema...')
else:
    print('Usuário ou senha inválidos...')
