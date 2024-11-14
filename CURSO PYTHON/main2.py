turno = str.upper(input('Em qual turno você estuda:manhã,tarde ou noite'))
palavradificilparaopython = 'MANHÃ'

if turno == 'MANHA' or turno in palavradificilparaopython:
 print('Bom dia!')
elif turno == 'TARDE':
 print('Boa tarde!')
elif turno == 'NOITE':
    print('Boa noite!')
else:
 print('Não entendi')
