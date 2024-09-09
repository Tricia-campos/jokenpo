from adivinhacao1 import advinhacao
from jokenpo import jogo
from perguntas import quiz

print("Bem vindo ao console de jogos!!")

menu = ''' Escolha um número reefrente ao jogo que você desja:
1- Advinhaçâo
2- Jokenpo
3- Perguntas e respostas'''

entrada_usuario = input(menu)

if entrada_usuario == "1":
    advinhacao()
elif entrada_usuario == "2":
    jogo()
elif entrada_usuario == "3":
    quit()