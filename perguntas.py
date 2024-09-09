perguntas = ["Quais alimentos foram multiplicados?","Qual milagre aconteceu em uma festa de casamento?","De qual doença o cego de Jericó foi curado?"]

respostas = ["paes e peixes","transformou agua em vinho","cegueira"]

print("JOGO DE PERGUNTAS BÍBLICAS")
print("TEMA: MILAGRES DE JESUS")

i = 0
pontos = 0

while i < len(perguntas):
    resposta_usuario = input(f"{perguntas[i]} ").strip().lower() 
    
    if resposta_usuario == respostas[i].lower():  
        print("Parabéns!!!")
        pontos += 3
        i += 1
    else:
        print("Que pena, você errou!")
        pontos -= 1  
        denovo = input("Quer tentar mais uma vez? (s/n): ").strip().lower()
        if denovo != 's':
            i += 1  
print(f"Você conseguiu {pontos} pontos! Até a próxima.")