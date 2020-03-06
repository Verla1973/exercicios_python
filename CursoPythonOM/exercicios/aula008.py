nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
altura = float(input('Qual sua altura? '))
peso = float(input('Qual o seu peso? '))
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2


print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')
print(f'Sua idade é {idade} anos e nasceu em {ano_nascimento}')
print(f'Sua altura é {altura}cm...')
print(f'Seu peso é {peso} kgs e tem um IMC de: {imc:.3f}...')
