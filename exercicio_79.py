# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from operator import length_hint


valores_digitados = []
opcao = 's'
while opcao == 's':
    valor_numerico = int(input('Digite um valor numérico: '))
    valores_digitados.append(valor_numerico)
    opcao = ''
    opcao = str(input('Inserir mais valores? s/n: '))
    while opcao not in 'SsNn':
        opcao = str(input('Inserir mais valores? s/n: '))
    if opcao in 'Nn':
        print('Programa finalizado.\nValores Digitados: ', end='')
        for i in range(length_hint(valores_digitados)):
            print(valores_digitados[i], end=', ')
        print('Fim.')
        break

            






