pizza = 0
faturamento = 0
maior_venda = 0
menor_venda = 0
acima_50 = 0

while True:
    valor = float(input("valor da pizza vendida (0 para encerrar) R$ "))
    if valor == 0:
        break
    if valor < 0:
        print("Valor invalido! Digite um valor positivo: ")
        continue
    pizza += 1
    faturamento += valor
    if valor > maior_venda: #na primeira venda, ele é maior
        maior_venda = valor
    if valor == 1 or valor < menor_venda:
        menor_venda = valor
    if valor > 50:
        acima_50 += 1
# print(f"esse foi o utlimo valor da variavel pizza no while: {pizza}")
# print(f"esse foi o ultimo valor da variavel faturamento no while: {faturamento:.2f}")
# print(f"esse é o valor da variavel valor (existe somente no while) {valor}")
if pizza == 0: # o laço precisa terminar para verificar, se estiver dentro o valor nunca vai ser zero, por isso precisa esta fora do laço 
    print("nehuma venda registrada hoje.")
else:
    tickt_medio = faturamento / pizza
    print("=== FECHAMENTO DO CAIXA ===")
    print(f"Pizzas vendidas: {pizza}")
    print(f"Faturamento total: R${faturamento:.2f}")
    print(f"Ticket medio:  R${tickt_medio:.2f}")
    print(f"Maior venda: R${maior_venda:.2f}")
    print(f"Menor venda: R${menor_venda:.2f}")
    print(f"pizzas acima de R$50.00 {acima_50}")


    # and -> ambos True
    # or -> um true => true
    #Verificar se o valor é 0(encerrar o sistema e não contar como valor de pizza)
    #Verificar se é positivo ou não(valor correto)