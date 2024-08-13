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
jogador = int(input('Qual é a sua escolha ?'))
print('*' *10)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('*' *10)


# print('O computador escolheu {}'.format(itens[computador]))