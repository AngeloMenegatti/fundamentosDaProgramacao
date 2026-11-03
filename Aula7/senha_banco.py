"""
(outra maneira de fazer um comentario)
crie um sistema q peça o usuario para digitar uma senha para acessa sua conta bancaria. Ele tem **apenas 3 tentativas** para acertar a senha.
se ele errar as 3 tentativas, o sistema bloqueia a conta.
- A senha correta 1234;
-se errar 3 vezes, conta bloqueia.
-o usuario tem 3 tentativas impit() 
"""
#variaveis no escopo global.
SENHA_CORRETA = "1234" #constante, boa pratica em python.
tentativas = 3 #uma variavel contadora, pode ser i ou j.

while tentativas > 0:
    senha = input("digite a sua senha: ") #variavel no escopo local(identado)
    if senha == SENHA_CORRETA:
        print("🔓 Acesso Permitido!")#windos + . = emoji
        break #comando que finaliza o loop.
    else:
        tentativas -= 1#forma compacta   #tentativas = tentativas -1
        print(f'senha incorreta. tentavias restantes: {tentativas}')
    if tentativas == 0:
        print("🔒 conta bloqueada.")