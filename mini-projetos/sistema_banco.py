# Funcionalidades
# - Saldo: Iniciar com um saldo de 0.0
# - Depósito: Permitir ao usuário depositar um valor, adicionando-o ao saldo.
# - Saque: Permitir ao usuário sacar um valor. Se o saldo for insuficiente, mostrar uma mensagem de erro.
# - Loop: Continuar no menu até que o usuário escolha "Sair".

import os
saldo_valor = 0.0

NOME_SALDO = 'Saldo'
NOME_DEPOSITO = 'Deposito'
NOME_SAQUE = 'Saque'

def exibir_nome_programa():
    print('''
    Sistema de Banco\n''')

# opções
def exibir_opcoes():
    print(f'1. {NOME_SALDO}.')
    print(f'2. {NOME_DEPOSITO}.')
    print(f'3. {NOME_SAQUE}.')
    print('4. Sair\n')

# finalizar o app
def finalizar_app():
    exibir_subtitulo('Finalizando...') #refatorando o código

# voltando para o menu principal
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    os.system('cls')  # limpa a tela antes de voltar ao menu

# quando a opção que o usuário submeteu for invalida
def opcao_invalida():
    print('\nOpção invalida.')

# refatorando a ação limpar tela + nome da ação
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto.upper().center(50))
    print()

# operação de saldo
def saldo():
    exibir_subtitulo(f'{NOME_SALDO}')
    print(f'Saldo da conta: {saldo_valor:.2f}')
    voltar_ao_menu()

# operação de deposito
def deposito():
    global saldo_valor
    exibir_subtitulo(f'{NOME_DEPOSITO}')
    try:
        deposito_valor = float(input('Informe o valor a ser depositado: '))
        if deposito_valor > 0:
            saldo_valor += deposito_valor
            print('\nOperação concluída. Depósito realizado com sucesso!')
        else:
            print('\nO valor do depósito deve ser positivo.')
    except:
        print('Erro: Valor inválido. Por favor, digite um número.')
    voltar_ao_menu()

# operação de saque
def saque():
    global saldo_valor
    exibir_subtitulo(f'{NOME_SAQUE}')
    while True:
        try:
            saque_valor = float(input('Informe o valor a ser sacado: '))
            if saque_valor <= 0:
                print('O valor do saque deve ser positivo.')
            elif saque_valor > saldo_valor:
                print(f'Operação inválida. Saldo disponível: {saldo_valor:.2f}.')
            else:
                saldo_valor -= saque_valor
                print('\nOperação concluída. Saque realizado com sucesso!')
                break
        except:
            opcao_invalida()
    voltar_ao_menu()

# escolhas
def escolher_opcao():
    while True:
        exibir_nome_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                case 1:
                    saldo()
                case 2:
                    deposito()
                case 3:
                    saque()
                case 4:
                    finalizar_app()
                    break
                case _:
                    opcao_invalida()
        except ValueError: 
            print('\nEntrada inválida. Por favor, digite um número.')
            voltar_ao_menu()

# função principal
def main():
    escolher_opcao()

# ponto de entrada do programa
if __name__ == '__main__':
    main()
