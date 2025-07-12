# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    calculo_desconto = preco * (1 - descontos.get(cupom))
    print(f'{calculo_desconto:.2f}')
else:
    print('Cupom não valido.')