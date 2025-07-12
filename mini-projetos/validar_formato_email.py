# Regras:
# - Deve conter o caractere '@' e um domínio como gmail.com ou outlook.com.
# - Não pode começar ou terminar com '@'
# - Não pode conter espaços. 


#  Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
dominios_permitidos = ['gmail.com', 'outlook.com']
valido = True

if ' ' in email:  # - Não pode conter espaços. 
    valido = False

if valido and (email.startswith('@') or email.endswith('@')):  # - Não pode começar ou terminar com '@'
    valido = False

if valido and '@' not in email:
    valido = False
else:
    if valido:
        partes = email.split('@')  # Separando a string para poder comparar o dominio
        dominios_encontrado = partes[1]
        if dominios_encontrado not in dominios_permitidos:  # - Deve conter o caractere '@' e um domínio como gmail.com ou outlook.com.
            valido = False

if valido:
    print('E-mail válido')
else:
    print('E-mail inválido')

