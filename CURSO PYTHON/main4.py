valorinicial = int(input('Digite o valor inicial:')) 
valorfinal = int(input('Digite o valor final:'))

for i in range(valorinicial, valorfinal+1):
    print(i)
    if i == valorfinal:
        break

