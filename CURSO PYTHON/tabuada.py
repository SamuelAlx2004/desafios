multilinha = '------------------------------------------'

numero = int(input(
    f'{multilinha}\n\n'
    f'              BRINCADEIRA\n'
    f'                  DA\n'
    f'                TABUADA\n\n'
    f'{multilinha}\n\n'
    f'Por favor, digite um número para a tabuada: '
))

print('\n')

for i in range(10, -1, -1):
    resultado = numero * i
    print(F'{numero} x {i} = {resultado}\n')
 