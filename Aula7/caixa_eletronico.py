""""
Crie um programa que simule um caixa eletronico.
O usuario pode sacar valores ate que o saldo disponivel
acabe ou até ele digitar 'sair'.
-comece com o saldo inicial de R$500.
-peça ao usuario digitar u, valot para saque:
- se o valor fpr maior que o saldo, avise que não ha saldo suficiente.
-se o usuario digitar 'sair', encerre o programa.
"""

saldo = 500

while saldo > 0: # ira continuar ate ser false(acabar o saldo) ou digitar 'sair'
    print(f'\n 💵Saldo disponivel: R${saldo:.2f}') #\n quebra a linha
    saque = input("digite o valot para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair": # O metodo lower() trasforma a string em minuscula.
        print("🏧 Operação encerrada.")
        break
    
    saque = float(saque)
    if saque > saldo:
        print("❌ Saldo insuficiente!")
    else:
        #saldo = saldo - saque
        saldo -= saque
        print("saque de R$:{saque:.2f} realizado com sucesso!")

