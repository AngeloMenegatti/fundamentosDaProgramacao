#exercicio 01

distancia = float(input("Distancia em km: ")) 
# if distancia <= 5:
#     print("R$5.00")

# elif distancia <= 10:
#     print("R$10.00")

# else: 
#     print("não sera possivel fazer a entrega")

#exercio 02


if distancia <= 5:
    print(5 + distancia * 1)
elif distancia <= 10:
    print(5 + distancia * 2)
else:
    print("Muito longe!")    

#exercicio 03

dia = input("Dia da semana: ").lower()
valor = float(input("Valor do pedido: R$ "))
# frete = 5
desconto = 15
desconto_valor = valor * desconto / 100

if dia == "terça" and valor > 40:
    print("Você ganhou uma sobremesa")
    print( valor + distancia)
elif dia == "quarta":
    print(f"""Parabens! hoje você ganhou um disconto de 15%, seu pedido saiu por!: {distancia + valor - desconto_valor}""")
elif dia == "sabado" or dia == "domingo" and valor >= 100:
    print("Frete Gratis!")
    print(valor)
elif dia == "segunda" or dia == "quinta":
    print("Hoje não tem promoção!")
    print(valor + distancia)   
else:
    print("Aconteceu um erro, tente novamente!")
 # esse exercicio foi feito na aula passada!


