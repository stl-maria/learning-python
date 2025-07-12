menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

saldo = 0.0
limite_valor = 500.0
extrato = '--- EXTRATO BANCÁRIO ---\n'
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # Depositar
    if opcao == 'd':
        try:
            deposito = float(input('Informe o valor a ser depositado: '))
            if deposito > 0:
                saldo += deposito
                print('\nDeposito feito com sucesso!')
                linha_extrato = f'Deposito: R$ {deposito:.2f}. Saldo: R$ {saldo:.2f}.\n'
                extrato += linha_extrato
            else:
                print('Informe um valor positivo.')
        except ValueError:
            print('\nValor invalido. Digite um número.')

    # Sacar
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('\nVocë atingiu o número máximo de saques diario.')
        else:
            try:
                saque = float(input('Informe o valor a ser sacado: '))

                if saque <= 0:
                    print('\nOperação falhou! Digite um valor positivo.')
                elif saque > saldo:
                    print('\nOperação falhou! Valor superior ao saldo atual.')
                elif saque > limite_valor:
                    print(f'\nOperação falhou! O valor do saque excede ao limite de R$ {limite_valor:.2f}')
                else:
                    saldo -= saque
                    numero_saques += 1
                    print('\nSaque feito com sucesso!')
                    linha_extrato = f'Saque: R$ {saque:.2f}. Saldo: R$ {saldo:.2f}.\n'
                    extrato += linha_extrato
            except ValueError:
                print('\nValor invalido. Digite um número.')

    # Extrato
    elif opcao == 'e':
        if extrato == '--- EXTRATO BANCÁRIO ---\n':
            print(extrato)
            print('Nenhuma operação realizada.')
        else:
            print(extrato)
            print(f'Saldo atual: {saldo:.2f}')

    # Sair
    elif opcao == 'q':
        print('Saindo...')
        break
    else:
        print('Opção invalida.')