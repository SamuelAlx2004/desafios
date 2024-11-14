lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
quantidadelista = len(lista)
total = 0

for i in range(0, quantidadelista):
    if lista[i] > 3000:
        total += 1

print(total)