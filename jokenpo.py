import random

def jogar_novamente():
    while True:
        jogar_denovo = input("Deseja jogar mais uma vez? (s/n): ").strip().lower()
        if jogar_denovo == 's':
            return True
        elif jogar_denovo == 'n':
            print("Obrigado por jogar!")
            return False
        else:
            print("Resposta inválida. Por favor, escolha 's' para sim ou 'n' para não.")

def jogo():
    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
        opcoes = ["pedra", "papel", "tesoura"]
        computador = random.choice(opcoes)
        print("JOKENPO!")
        print() # espaço    
        usuario = input("Escolha pedra, papel, tesoura ou 'x' para sair: ").lower()

        if usuario == "x":
            print("Jogo encerrado")
            break
        
        if usuario not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"O computador escolheu: {computador}")

        if usuario == computador:
            print("Empate")
            empates += 1
        elif (usuario == 'tesoura' and computador == 'papel') or \
             (usuario == 'pedra' and computador == 'tesoura') or \
             (usuario == 'papel' and computador == 'pedra'):
            print("Você venceu")
            vitorias += 1
        else:
            print("Você perdeu")
            derrotas += 1

    print(f"Vitórias: {vitorias} / Derrotas: {derrotas} / Empates: {empates}")

while True:
    jogo()
    if not jogar_novamente():
        break