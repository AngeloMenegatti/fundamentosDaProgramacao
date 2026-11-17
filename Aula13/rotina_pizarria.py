#Primeira função, calcular_preco_pizza()
def Calcular_preco_pizza(tamanho):
    tabela = { "p": 25.0,"m": 35.0,"g": 45.0,}
    "para receber o valor você acessa a key do dicionário, que é o tamanho da pizza"
    return tabela.get(tamanho, 0)
    "tabela.get é uma forma segura de acessar valores no dict"
    ".get(tamanho, 0) evita retorno none se a chave existir, retornando 0 caso não exista"

# print(Calcular_preco_pizza("p"))

#segunda função, calcular_taxa_entrega()
def Calcular_taxa_entrega(distancia_km):
    if distancia_km <= 3:
        return 5.0
    elif distancia_km <= 7:
        return 10.0
    else:
        return 15.0

# print(Calcular_taxa_entrega(5))

#terceira função, aplicar_deconto_fidelidade()
def Aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel):
    if eh_cliente_fiel:
        return subtotal * 0.90  # Aplica desconto de 10%
    return subtotal  # Sem desconto

# print(Aplicar_desconto_fidelidade(100, True))

def fechar_pedido(tamanho, distancia_km, eh_cliente_fiel): #Essa função REUTILIZA todas as funções anteriores para calcular o preço final do pedido
    preco_pizza = Calcular_preco_pizza(tamanho)
    taxa_entrega = Calcular_taxa_entrega(distancia_km)
    subtotal = preco_pizza + taxa_entrega
    total = Aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel)

    print(f"pizza ({tamanho})! R$ {preco_pizza:.2f}")
    print(f"Taxa de entrega: R$ {taxa_entrega:.2f}")
    print(f"total: R$ {total:.2f}")
    print("-"*30)


fechar_pedido("g", 5, True)

