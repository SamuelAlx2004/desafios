multilinha = '------------------------------------------'

titulo = (
    f'{multilinha}\n\n'
    f'        🟩 BRINCADEIRA 🟩\n'
    f'                DA\n'
    f'        🟩   TABUADA   🟩\n\n'
    f'{multilinha}\n\n'
)

numero = int(input(f'{titulo}Por favor, digite um número para a tabuada: '))

print("\n" + "🎉 Vamos começar a tabuada! 🎉\n")

for i in range(10, -1, -1):
    resultado = numero * i
    print(f' {numero} x {i} = {resultado}\n' + '-'*35)