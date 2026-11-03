# Estruturas comdicionais permitem que o programa execute blocos de codigo diferentes dependendo de uma condição. A condição é sempre avaliada com true(verdadeiro) False(falso)

# Se o usuario tiver a idade maior que 18, ele poderá entrar 
#if -> verifica uma condição e executa o bloco de codigo associado se a condição for verdadeira

idade_usuario = 21 # Hardcode
# if idade_usuario > 18:
#     print("o usuário pode acessar o local.")

# else -> permite executar o bloco de codigo se a condição if for falsa

# if idade_usuario > 18:
#     print("o usuário pode entrar no local.")
# else:
#     print("entrada proibida!")

#elif -> Abreviação (else if) é usado para testar várias condições.
# ele só será exibido se todos as condições anteriores forem falsas.

nota = int(input("digite a nota do aluno: "))
# nota maior ou igual a 90, "Aprovado com nota exelente"
# nota for maior ou igual a 70, "Aprovada"
# qualquer outra nota, será exibido "Reprovado"

if nota >= 90:
    print("Aprovado com nota excelente")
elif nota >= 70:
    print("aprovado")
else:
    print("reprovado kkkkkkk O-T-A-R-I-O")