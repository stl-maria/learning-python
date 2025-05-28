# 1.
# Comentário em uma linha
"""
Comentário em bloco,
mais utilizado para documentação
"""
'''
Com aspas simples
'''

# 2.
print(' Saída de dado '.center(30,'-'))

# função print()
print("Exemplo", "de", "texto")

#  argumentos da função print()
print("maçã", "laranja", "morango",sep=",\n", end=".\n")


# 3.
print(' String '.center(30,'-'))

string1 = "Exemplo de string" 
string_multipla = """Exemplo de string multipla,
se estende por
várias linhas.
"""

# métodos de strings
texto = "   O céu é azul! !"
print(texto.upper())
print(texto.lower())
print(texto.strip())  # tirá os espaços em branco no início e no fim apenas
print(texto.split())
print('-'.join(texto.split()))  # ou -> '-'.join(['O', 'céu', 'é', 'azul!', '!'])

# formatação string
nome = "Lucas"
idade = 29

# operador %
print("O nome dele é %s e ele tem %d anos." % (nome, idade))

# método format()
print("O nome dele é {} e ele tem {} anos.".format(nome, idade))

# f-string
print("O nome dele é {nome} e ele tem {idade} anos.")


# 4.
print(' Tipo de dados '.center(30,'-'))

# Primitivos
print("Ana", type("Ana"))
print(123, type(123))
print(13.4, type(13.4))
print(10 == 10, type(10 == 10))

# Conversão
numero = "10"  # str
convertido_p_numero = int(numero)  # convertendo para int
print(convertido_p_numero, type(convertido_p_numero))
print("Outro modo de converter diretamente",int(numero), type(int(numero)))

convertido_p_float = float(numero)  # convertendo para float
print(convertido_p_float, type(convertido_p_float))

numero_um = 1234  # int
convertido_p_texto = str(numero_um)  # convertendo para string
print(convertido_p_texto, type(convertido_p_texto))

convertido_p_booleano = bool(numero)  # convertendo para booleano
print(convertido_p_booleano, type(convertido_p_booleano))

# 5.
print(' Entrada de dados '.center(30,'-'))

nome_usuario = input('Informe seu nome: ')
print(f'Olá, {nome_usuario}! :D')