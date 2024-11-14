multilinha = '------------------------------------------'

titulo = (
    f'{multilinha}\n\n'
    f'        🟩     BRINCADEIRA    🟩\n'
    f'                   DOS\n'
    f'        🟩   NUMEROS PRIMOS   🟩\n\n'
    f'{multilinha}\n\n'
)

numero = int(input(f'{titulo}Por favor, digite um número: '))
listadivisores = []
condicaoprimo = [numero,1]

for i in range(1, numero + 1):
    if numero % i == 0:
        listadivisores.append(i)

if len(listadivisores) == 2:
    print(f'O {numero} é primo')
else:
    print('Esse numero não é primo')

print(listadivisores, condicaoprimo)
    

    
    
    


