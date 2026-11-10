def calcular_preco_pizza(sabor, tamanho, borda_recheada=False):
    "calcula o preço final de uma pizza com opções."
    tabela = {
        "p": 25.0,
        "m": 35.0,
        "g": 45.0
    }
    preco = tabela[tamanho]
    if borda_recheada:
        preco += 8.0
    print(f"""Preço da pizza de {sabor}
      tamanho é {tamanho}
      a borda é recheada?{borda_recheada}
      preço total: R$ {preco}""")
    # return preco, sabor



print(calcular_preco_pizza("frango", "g"))