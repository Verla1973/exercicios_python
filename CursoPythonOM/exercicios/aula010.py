nome = input('Digite o seu nome: ')
idade = int(input('Qual a sua idade: '))
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode solicitar empréstimo...')
else:
    print(f'{nome} não pode solicitar o empréstimo...')
