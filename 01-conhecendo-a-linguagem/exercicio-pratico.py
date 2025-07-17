menu = '''
Escolha qual exercicio deseja executar:

1 - Contador de vogais e consoantes
2 - Remove Caractere
3 - Palíndromo
4 - Par ou ímpar
5 - Ano bissexto
6 - Sair

==> '''


while True:
    opcao = input(menu)

    if opcao == '1':
        vogais = 'aeiou'
        qtd_vogais = 0
        qtd_consoantes = 0
        palavra = input('Informe uma palavra para contar as vogais e consoantes: ')

        for caractere in palavra:
            if caractere in vogais:
                qtd_vogais += 1
            if caractere not in vogais:
                qtd_consoantes += 1
            
        print(f'Quantidade de vogais: {qtd_vogais}.')
        print(f'Quantidade de consoantes: {qtd_consoantes}.')

    elif opcao == '2':
        texto = input('Informe uma palavra: ')
        caracter = input('Informe o caracter que deseja remover: ')

        print(f'{texto.replace(caracter, '')}')

    elif opcao == '3':
        verificar = input('Informe uma palavra: ')
        palindromo = True
        if verificar != verificar[::-1]:
            palindromo = False
        
        if palindromo:
            print('A palavra é um palíndromo.')
        else:
            print('A palavra não é um palíndromo.')
    elif opcao == '4':
        numero = int(input('Informe um número inteiro: '))
        if (numero % 2) == 0:
            print('O número é par.')
        else:
            print('O número é ímpar.')
    elif opcao == '5':
        ano = int(input('Informe um ano: '))
        bissexto = True
        if (ano % 4) != 0:
            bissexto = False

        if ano and (ano % 100 == 0):
            bissexto = False

        if bissexto:
            print(F'O ano {ano} é bissexto.')
        else:
            print(f'O ano {ano} não é bissexto.')

    else:
        print('Saindo...')
        break
            
    