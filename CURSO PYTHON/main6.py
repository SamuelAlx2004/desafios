quantidade_avaliacao = int(input('Informe a quantidade de dados: '))
contador = 0
numeros_validos = (0, 1, 2, 3, 4, 5)

while contador < quantidade_avaliacao:
    nota = int(input('Digite a nota da avaliação (0-5): ').strip())

    if nota in numeros_validos:
        contador += 1
        print(f'NOTA VALIDA\nID: {contador}\nNOTA: {nota}\n-----------------')
    else:
        print('VALOR INVALIDO. REPITA A NOTA')
