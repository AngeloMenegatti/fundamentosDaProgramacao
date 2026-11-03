#sabores = ["Mussarela", "Calabresa", "Pepperoni", "Quatro Queijos", "Frango com Catupiry"]

# print("Sabores disponíveis na Pizzaria Sabores:")
# for sabor in sabores:
#     print(f"🍕- {sabor}")

# 3) Usando range() para repetição controlada

# print("Preparando sua pizza...")
# for minuto in range(1, 6): #no range o ultimo numero é exclusivo, então na real vai de 1 á 5
#     print(f"{minuto} minuto(s) se passou...")

# print("Sua pizza está pronta! Bom apetite!")

#4) break e continue para controle de fluxo

# clientes = ["João", "Maria", "Carlos", "Ana", "Pedro"] # a posição sempre começa do zero, então a conta da lista é 0,1,2,3,4

# print("Atendendo clientes:")
# for i, cliente in enumerate(clientes): #O python ja espera que a primeira variavel seja referente a posição, no caso a variavel i
#     if i == 3: # O i esta sendo usando como uma variavel para guaradar a possição 
#         print("Capacidade máxima atingida! Não podemos atender mais clientes agora.")
#         break
#     print(f"Atendendo {cliente}...")

#E o continue? Pulando um item da fila

pedidos = ["Mussarela", "cancelado", "Calabresa", "cancelado", "Pepperoni"]

for pedido in pedidos:
    if pedido == "cancelado":
        continue  # pula este e vai para o próximo
    print(f"Preparando pizza de {pedido}...")

