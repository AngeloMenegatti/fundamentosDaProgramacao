#comandos principais do python

Printi() - exibe informaçoes no terminal
input() - exibe e/ou recebe informação
f""" """ - f-string. concatena variaveis e textos

ctrl + : = cria comentario 

# cases utilizados nas linguagens de programação
1. cammelCase. Ex: nomeDoUsuario
2. PascalCase. Ex: NomeDoUsuario
3. """snake_case. Ex: nome_do_usuario"""(preferncia de uso)
4. Kebab-case. Ex: nome-do-usuario

# Python não tem constante, mas tem boa prática.
CPF = 123456 # constante, boa prática (letra maiuscula)

# operadores matematicos
+ -> Adição
- -> subtração
* -> multiplicação
/ -> divisão
// -> divisão inteira
% -> resto da divisão (módulo)
** -> exponenciação (potência)

# operadores logicos
and -. retorna true se ambos forem verdadeiros
or -> retorna true se um ou ambos forem verdadeiros
not -> Inverte o valor lógico
# operadores de comparação
== -> igual a
!= -> diferente de
< -> menor que
> -> maior que
<= menor ou igual a
>= maior ou igual a

# Escopo global % escopo loccal
>Global:
pode ser acessada por qualquer parte do sistema. No entanto, em Python ela
escapa. O valor da variavel global é modificada em alguma estrutura
e o valor fica sendo o ultimo usado nessa estrutura.
>Local:
Ela é criada dentro de uma estrutura. Ela vale somente naquela estrutura e
se em u  outro nivel(dentro de um if) ela ser utilizada, ela escapa porém pode reutilizada

# funções [def]
-> é um objeto guardado numa variavel, que contem um bloco de codigo ainda não executado.
quando voce a chama, o python cria um espaço de nomes novos e temporarios.
[def] -> palavra-chave que inicia a declaração da função.
[nome_funcao] -> identificador - utilizando o padrão """snake_case"""
[parametros] -> dados de entrada entre parêmtesses.
[argumentos] -> Valores que ocupam o lugar dos parâmetros.
[docstring] -> documentação entre aspas duplas.
[corpo] -> bloco identado contendo a logica da função.
[return] -> valor retornado, se a def não tiver o return, o padrão é none.