"""
01 - Conhecendo a Linguagem Python
Este arquivo contém uma introdução à linguagem Python com explicações básicas
e exercícios para prática.
"""

# - Comentários em Python
# Para uma linha inicie com #
# Para várias linhas -> """ ou '''

# - Sáida de dados
print('Olá, mundo')

# - Tipo de dados
nome = 'Estela'  # str
idade = 25  # int
altura = 1.55  # float
ativo = True  # bool


# - Argumentos nomeados
print(nome,idade,altura,ativo, sep=" | ", end="\nFim\n")

# - Entrada de dados
nome_usuario = input('Qual o seu nome? ')