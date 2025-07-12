menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

saldo = 0.0
limite_valor = 500.0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # Depositar:
    if opcao == 'd':
        try:
            deposito = float(input('Informe o valor a ser depositado: '))
            if deposito > 0:  # Condicional para depositar apenas valores positivos.
                saldo += deposito
                print('\nDeposito feito com sucesso!')
                extrato += f'Depósito: R$ {deposito:.2f}.\n'  # Concatenando no extrato.
            else:
                print('Informe um valor positivo.')
        except ValueError:
            print('Valor invalido. Digite um número.')

    # Sacar:
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:  # Condicional para limites de saques diários.
            print('\nVocê atingiu o número máximo de saques diario.')
        else:
            try:
                saque = float(input('Informe o valor a ser sacado: '))
                if saque <= 0:  # Condicional quando o valor do saque for menor ou igual a 0. 
                    print('\nOperação falhou! Digite um valor positivo.')
                elif saque > saldo:  # Condicional quando o valor do saque for maior que o saldo atual.
                    print('\nOperação falhou! Valor superior ao saldo atual.')
                elif saque > limite_valor:  # Condicional quando o valor do saque for maior que o limite para a transação.
                    print(f'\nOperação falhou! O valor do saque excede ao limite de R$ {limite_valor:.2f}')
                else:
                    saldo -= saque
                    numero_saques += 1  # Contagem de quantidade de saques.
                    print('\nSaque feito com sucesso!')
                    extrato += f'Saque: R$ {saque:.2f}.\n'  # Concatenando no extrato.
            except ValueError:
                print('Valor invalido. Digite um número.')

    # Extrato
    elif opcao == 'e':
        print('--- EXTRATO BANCÁRIO ---\n')  # Cabeçalho
        print('Não foram realizadas movimentações.\n' if not extrato else extrato)  # Condicional para verificar se o extrato está vazio.
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('--------------------------')  # Rodapé

    # Sair
    elif opcao == 'q':
        print('Saindo...')
        break  # Saindo do loop.
    else:
        print('Opção invalida.')