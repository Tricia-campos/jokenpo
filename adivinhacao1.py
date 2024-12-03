import random
def advinhacao():
    alvo = random.randint(0, 100)
    numero_tentativas = 5
    print("JOGO DE ADIVINHÇÃO")

    while numero_tentativas > 0:
        try:
            chute = int(input("Digite um número entre 0 e 100: "))
            if chute < 0 or chute > 100:
                print("Número invalido!!")
            elif chute == alvo:
                print(" parabéns, você acertou!!!")
                break
            else:
                if numero_tentativas > 1:
                    if chute > alvo:
                        print("tente um número menor: ")
                    else:
                        print("tente um número maior: ")

            numero_tentativas = numero_tentativas -1

        except:
            print("Digite um número inteiro. ")

        if numero_tentativas == 0:
            print(f"Você perdeu! O número era {alvo}. ")



def conseguiu():
    vitorias = 0
    derrotas = 0

    while True:
        acertou = advinhacao()
        if acertou:
            vitorias += 1
        else:
            derrotas += 1
        print(f"vitorias: {vitorias} / derrotas: {derrotas}")
        break


    jogar_denovo = str(input(" Deseja jogar mais uma vez? (s/n): ")).strip().lower()
    if jogar_denovo != 's':
            print("Obrigado por jogar!")


conseguiu()