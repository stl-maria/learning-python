import os

def exibir_nome_programa():
    print('''
    Exercicios
    Selecione qual deseja ver:\n''')

# opções
def exibir_opcoes():
    print('1. Calculadora.')  # 3
    print('2. Classificador de idade.')  # 3
    print('3. Inversor de palavras.')  # 4
    print('4. Contador de vogais.')  # 3 
    print('5. Tabuada personalizada')  # 3
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

########################################################################

# Exercicios:
def ex_calculadora():
    exibir_subtitulo('1. Calculadora Simples')

    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))

    print(f'Soma: {x + y}')
    print(f'Subtração: {x - y}')
    print(f'Multiplicação: {x * y}')

    if y != 0:
        print(f'Divisão: {(x / y):.2f}')
    else:
        print('Não é possível realizar divisão por zero.')

    voltar_ao_menu()

def ex_classifica_idades():

    exibir_subtitulo('2. Classificador de Idade')
    idade = int(input('Qual a sua idade? '))

    if idade >= 0 and idade < 13:
        classificador = 'Criança'
    elif idade < 18:
        classificador = 'Adolescente'
    elif idade < 61:
        classificador = 'Adulto'
    elif idade > 60:
        classificador = 'Idoso'
    else:
        opcao_invalida()

    print(f'Você é {classificador}.')
    
    voltar_ao_menu()

def ex_inversor_palavras():

    exibir_subtitulo('3. Inversor de Palavras')
    texto = input('Digite uma palavra: ')
    print(f'{texto[::-1]}')

    voltar_ao_menu()

def ex_contador_vogais():

    exibir_subtitulo('4. Contador de Vogais')
    vogais = 'aeiouAEIOU'

    frase = input('Digite uma frase: ')
    contador_vogais = 0

    for caractere in frase:
        if caractere in vogais:
            contador_vogais += 1
    
    print(f'Número de vogais: {contador_vogais}')
    voltar_ao_menu()


def ex_tabuada():

    exibir_subtitulo('5. Tabuada Personalizada')
    tabuada = int(input('Digite um número para tabuada: '))
    i = 0
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    voltar_ao_menu()

########################################################################

# quando a opção desejada é selecionada
def escolher_opcao():
    while True:
        exibir_nome_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                case 1:
                    ex_calculadora()
                case 2:
                    ex_classifica_idades()
                case 3:
                    ex_inversor_palavras()
                case 4:
                    ex_contador_vogais()
                case 5:
                    ex_tabuada()
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