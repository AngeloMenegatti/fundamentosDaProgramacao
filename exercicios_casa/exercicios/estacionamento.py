idade = float(input("Inserir idade: "))
vip = input("É VIP? ").lower()
cadastro = input("tem cadastro? ").lower()
tipo_veiculo = input("informe o tipo de veiculo: carro, moto, caminhão: ")

if idade < 18:
    print("entrada negada")
elif vip == "sim" and cadastro == "sim":
    print("Bem vindo vip!")
elif cadastro == "sim" and vip == "não": 
    print("Bem vindo")
elif tipo_veiculo == "caminhão":
    print("entrada negada")
elif idade < 22:
    print("entrada permitida com auxilio de um funcinario")
elif idade >= 23:
    print("Bem vindo")
else:
    print("entrada negada")