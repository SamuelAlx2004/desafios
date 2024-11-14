numerofatorial = int(input('Digite o valor e descubra o seu valor fatorial: '))
fatorial = 1  

for i in range(numerofatorial, 0, -1):
    fatorial *= i  

print(f"O fatorial de {numerofatorial} é {fatorial}.")
