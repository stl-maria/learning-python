import os

def exibir_nome_programa():
    print('''
    Exercicios
    Selecione qual deseja ver:\n''')

# opções
def exibir_opcoes():
    print('1. Inversor de palavras.')  
    '''print('2. ') 
    print('3. ')  
    print('4. ')  
    print('5. ')'''
    print('6. Sair\n')

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
    print(texto)
    print()



# Exercicios:
def ex_inversor_palavras():

    exibir_subtitulo('3. Inversor de Palavras')
    texto = input('Digite uma palavra: ')
    print(f'{texto[::-1]}')

    voltar_ao_menu()



# quando a opção desejada é selecionada
def escolher_opcao():
    while True:
        exibir_nome_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                case 1:
                    ex_inversor_palavras()
                case 6:
                    finalizar_app()
                    break  # sai do loop
                case _:
                    opcao_invalida()
        except:
            opcao_invalida()
            voltar_ao_menu()

def main():
    escolher_opcao()

# main
if __name__ == '__main__':
    main()