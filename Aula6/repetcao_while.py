sabores_pizza = ["mussarela","calabresa","pepperoni","quatro queijo", "frango com catupiry"]
print("faça seu pedido (digite 'sair' para encerrar): ")
pizza = "" # Aqui ficará armazenado a pizza do cliente

# Enquanto o sair nõa for digitado, o while continuará sendo executado.
while pizza.lower() != "sair":
    pizza = input("Escolha um sabor: ").lower()
    if pizza in sabores_pizza:
        print(f'{pizza} foi adicionado ao sua compra.')
    elif pizza.lower() == "sair":
        print("pedido encerrado!")
    else:
        print("Esse sabor não está no cardápio. Escolha outro: ") 

