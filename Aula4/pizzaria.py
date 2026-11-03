# Oerguntas a serem feitas ao cliente
# Pizza pequena 19.90
# pizza média = 29.90
#pizza grande = 39.90
# Comprado qualquer pizza e qualquer tamanho so sabado o refri é gratuito

FRETE = 2
dia_semana = "segunda"
print(f"""
    ======================
    Seja bem-vindo a pizzaria Jão
    ======================
""")

nome_cliente = input(f"""
    digite o seu nome:

""")
pizza_sabor = input(f"""

    Escolha uma das opções abaixo:
     1- para frango com requeijão
     2- para calabresa
     3- musarela
     4- banana com chocolate
     """)

pizza_tamanho = input(f"""
    escolha p tamanho da pizza:
    1- pequena
    2- media
    3- grande
""") 

forma_entrega = input(f"""
    escolha a forma de entrega:
    1- comsumo no local
    2- entrega na residência
""")

# estrutura condicional para promoção
# Comprado qualquer pizza e qualquer tamanho so sabado o refri é gratuito
#comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratis
#comprando uma pizza de calabresa tamanho medio, em qualquer dia, o frete e gratis

if dia_semana == "sabado":
    print(f"pedido aceito com sucesso!")
    print(f"o refri hoje é gratis")
elif dia_semana == ("domingo"):    
    print(f"pedido aceito com sucesso!")
    print(f"o refri e o frete hoje é gratis")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
     print(f"pedido aceito com sucesso!")
     print(f"o frete hoje é gratis")



# print(f"""
#     ======================
#          Resumo do pedido
#          Nome do cliente: {nome_cliente}
#          Sabor da pizza: {pizza_sabor}
#          Tamanho da pizza: {pizza_tamanho}
#          Forma de entrega: {forma_entrega}
#     ======================

# """)