from random import randrange

multilinha = '------------------------------------------'
titulo = (
    f'{multilinha}\n\n'
    f'        ♠       🎰🎰🎰        ♦\n'
    f'        ♦       SORTEIO       ♠\n\n'
    f'{multilinha}\n\n'
)

print(titulo)

listacandidatos = []
res = None

while res != 'STOP':
    res = input('INFORME O NOME DOS PARTICIPANTES UM DE CADA VEZ\nE PARA FINALIZAR DIGITE STOP: ').upper().strip()
    listacandidatos.append(res)

    if res != 'STOP':
        print(f'\n{res} FOI ADICIONADO COM A SENHA {len(listacandidatos)}\n')
    else:
        print(f'\nFINALIZADO!\n')

listacandidatos.remove('STOP')
print(listacandidatos)

vencedor = randrange(len(listacandidatos))

print(F'\n🎉  O VENCEDOR FOI {listacandidatos[vencedor]} COM A SENHA {vencedor+1}  🎉\n')