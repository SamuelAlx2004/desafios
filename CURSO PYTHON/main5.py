bacteriaA = 4
bacteriaB = 10
dia = 0

while bacteriaA < bacteriaB:
    dia += 1
    bacteriaA *= 1.03
    bacteriaB *= 1.015

    print(f'DIA: {dia}\n Bactéria A: {bacteriaA}\n Bactéria B: {bacteriaB}\n----------------------')
