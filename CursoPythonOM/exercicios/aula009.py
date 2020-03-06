nota = float(input('Digite uma nota:'))

if (nota > 9):
    nome = input('Digite o nome do aluno: ')
    print(f'Aluno {nome} aprovado com Quadro de Honra...')
elif (nota >= 8):
    nome = input('Digite o nome do aluno: ')
    print(f'Aluno {nome} aprovado com notas boas...')
elif (nota >= 7):
    nome = input('Digite o nome do aluno: ')
    print(f'Aluno {nome} aprovado...')
elif (nota >= 4):
    nome = input('Digite o nome do aluno: ')
    print(f'Aluno {nome} em recuperação...')
else:
    nome = input('Digite o nome do aluno: ')
    print(f'Aluno {nome} Reprovado...')
print('Fim...')
