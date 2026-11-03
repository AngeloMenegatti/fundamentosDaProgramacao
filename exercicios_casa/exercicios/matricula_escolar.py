idade =  int(input("Inserir idade: "))
nota =  float(input("Inserir nota: "))
frequecia =  float(input("Inserir frequência: "))

if idade < 18:
    print("matricula negada. Aluno menor de idade.")
elif nota <= 5:
    print("Nota insuficiente")
elif nota >= 9:
    print("Aprovado automaticamente")
elif idade >=18 and nota >= 6 and frequecia >= 75:
    print("Matricula Aprovada")
else:
    print("Matricula negada.")