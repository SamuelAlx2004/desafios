valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    maiorvalor = valor1
    if valor2 > valor3:
        segundomaiorvalor = valor2
        terceirovalor = valor3
    else:
        segundomaiorvalor = valor3
        terceirovalor = valor2
elif valor2 > valor1 and valor2 > valor3:
    maiorvalor = valor2
    if valor1 > valor3:
        segundomaiorvalor = valor1
        terceirovalor = valor3
    else:
        segundomaiorvalor = valor3
        terceirovalor = valor1
else:
    maiorvalor = valor3
    if valor1 > valor2:
        segundomaiorvalor = valor1
        terceirovalor = valor2
    else:
        segundomaiorvalor = valor2
        terceirovalor = valor1   

print(f'{maiorvalor}, {segundomaiorvalor}, {terceirovalor}')
