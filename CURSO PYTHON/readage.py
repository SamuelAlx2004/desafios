multilinha = '------------------------------------------'
titulo = (
    f'{multilinha}\n\n'
    f'        🟩      REGISTRO     🟩\n'
    f'                   DE\n'
    f'        🟩       IDADES      🟩\n\n'
    f'{multilinha}\n\n'
)

lista_0_25 = []
lista_26_50 = []
lista_51_75 = []
lista_76_100 = []
idade = 1

while idade > 0:
    idade = int(input(f'{titulo}Por favor, digite um número: '))
    match idade:
        case n if n > 0 and n <= 25:
            lista_0_25.append(idade)
        case n if n > 25 and n <= 50:
            lista_26_50.append(idade)
        case n if n > 51 and n <= 75:
            lista_51_75.append(idade)
        case n if n > 76 and n <= 100:
            lista_76_100.append(idade)

print(f'-----| TABELA |-----\nTOTAL EM CADA LISTA\n[0 ATÉ 25]: {len(lista_0_25)}\n[26 ATÉ 50]: {len(lista_26_50)}\n[51 ATÉ 75]: {len(lista_51_75)}\n[76 - 100]: {len(lista_76_100)}')
    