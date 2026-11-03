idade =  float(input("Inserir idade: "))
salario =  float(input("Inserir salario: "))
tempo_empresa =  float(input("Inserir anos trabalhado na empresa: "))

if idade < 18:
   print("Empréstimo  negado.")
elif  salario >= 5000:
    print("aprovado automaticamente")
elif tempo_empresa < 2:
    print("não")
elif salario < 2000:
    print("não aprovado")
elif idade >= 18 and salario >= 2000 and tempo_empresa >= 2:
    print("Empréstimo aprovado")
else:
    print("negado")
