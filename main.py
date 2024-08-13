# Importando modulo Random
from random import randint 

# Opções de escolha
itens = ('Pedra', 'Papel', 'Tesoura')

# Maquina escolha randomica
computador = randint(0, 2)

# Opções do Jogador 
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

# Entrada do usuário
jogador = int(input('Qual é a sua escolha? '))
print('*' *10)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('*' *10)

# Estrutura condicional
if computador == 0:  # Computador escolheu PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador Vence!')
elif computador == 1:  # Computador escolheu PAPEL
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence!')
elif computador == 2:  # Computador escolheu TESOURA
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate!')

