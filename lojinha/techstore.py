
notbook = ["macbook air ", "galaxy book4", "asus vivobook"]
valornb =["6300.00", "2768.67","2769.89"]
smartfones = ["iphone 15 pro max", "S23 ultra","moto edge 40" ]
valorsf =["9967.89", "4200.78", "4090.76"]
fone = ["airpods pro 3", "galaxy buds fe", "jbl"]
valorf =["1400.90","469.89","290.60"]

  
print("TECHSTORE")
cliente = input("Bem vindo a techstore, deseja conhecer nossas promoções? (sim/nao): ")
if cliente == "sim":
  print ("""   --------------------------------------------------------------
        | confira nossas promoções do dia:                           |
        |NOTBOOKS -> macbook air de 6999.90R$ por 6300.00R$          |
        |            galaxy book4 de 3999.90R$ por 2768.67R$         |
        |            asus vivobook de 2999.90R$ por 2769.89R$        |
        |SMARTONES -> iphone 15 pro max de 9999.90R$ por 9967.89R$   |
        |            S23 ultra de 4399.90R$ por 4200.78R$            |
        |            moto edge 40 de 4299.90R$ por 4090.76R$         |
        |FONE DE OUVIDO -> airpods pro 3 de 1499.90R$ por 1400.90R$  |
        |            galaxy buds fe de 500.90R$ por 469.89R$         |
        |            JBL de 299.90R$ por 290.60R$                    |
        --------------------------------------------------------------""")                
else:
    print("até a proxima! ")   


comprar = input(f"""Qual produto você deseja comprar? 
      Escolha uma opção:
      1.notbooks
      2. smartfones
      3. fone de ouvido: """)
      


if comprar == "1":
    print(notbook)
    produto1 = input("Qual produto dessa categoria vc deseja? (1/2/3): ")
    if produto1 == "1":
        print(f""" NOTA:
          O valor a ser pago é {valornb[0]}R$ """)
    elif produto1 == "2":
        print(f""" NOTA:
          O valor a ser pago é {valornb[1]}R$ """)
    elif produto1 == "3":
        print(f""" NOTA:
          O valor a ser pago é {valornb[2]}R$ """)
   

if comprar == "2":
    print(smartfones,valorsf)
    produto2 = input("Qual produto dessa categoria vc deseja? (1/2/3): ")
    if produto2 == "1":
        print(f""" NOTA:
          O valor a ser pago é {valorsf[0]}R$ """)
    elif produto2 == "2":
        print(f""" NOTA:
          O valor a ser pago é {valorsf[1]}R$ """)
    elif produto2 == "3":
        print(f""" NOTA:
          O valor a ser pago é {valorsf[2]}R$ """)

if comprar == "3":
    print(fone,valorf)
    produto3 = input("Qual produto dessa categoria vc deseja? (1/2/3): ")
    if produto3 == "1":
        print(f""" NOTA:
          O valor a ser pago é {valorf[0]}R$ """)
    elif produto3 == "2":
        print(f""" NOTA:
          O valor a ser pago é {valorf[1]}R$ """)
    elif produto3 == "3":
        print(f""" NOTA:
          O valor a ser pago é {valorf[2]}R$ """)
