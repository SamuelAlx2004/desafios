multilinha = '---------------------------------------------------'
titulo = (
    f'{multilinha}\n\n'
    f'        ⚖️     ELEIÇÃO                ⚖️\n'
    f'        ⚖️     CANDIDATOS:            ⚖️\n'
    f'        ⚖️     RITA: 2050             ⚖️\n'
    f'        ⚖️     ANDRADE: 1015          ⚖️\n'
    f'        ⚖️     SILVANIA: 1919         ⚖️\n'
    f'        ⚖️     LUCIANO: 5110          ⚖️\n'
    f'\n     OBSERVAÇÃO: INDIQUE NOME OU NUMERO DO\nCANDIDATO CASO UM ERRO SERA CONSIDERADO VOTO NULO\n'
    f'            E PARA BRANCO DIGITE BRANCO\n'
    f'{multilinha}\n\n'
)
print(f'{titulo}')

# CANDIDATOS
rita = {'nome': 'RITA', 'codigo': 2050}
andrade = {'nome': 'ANDRADE', 'codigo': 1015}
silvania = {'nome': 'SILVANIA', 'codigo': 1919}
luciano = {'nome': 'LUCIANO', 'codigo': 5110}

# LISTAS
listarita = []
listaandrade = []
listasilvania = []
listaluciano = []
nulos = []
branco = []

for i in range(1, 21):
    resposta = input('⚖️  INFORME CODIGO OU NOME DO CANDIDATO:  ').strip()
    if resposta.upper() == rita['nome'] or resposta == str(rita['codigo']):
        listarita.append(resposta)
    elif resposta.upper() == andrade['nome'] or resposta == str(andrade['codigo']):
        listaandrade.append(resposta)
    elif resposta.upper() == silvania['nome'] or resposta == str(silvania['codigo']):
        listasilvania.append(resposta)
    elif resposta.upper() == luciano['nome'] or resposta == str(luciano['codigo']):
        listaluciano.append(resposta)
    elif resposta.upper() == 'BRANCO':
        branco.append(resposta)
    else:
        nulos.append(resposta)

total = len(listarita) + len(listaandrade) + len(listasilvania) + len(listaluciano) + len(nulos) + len(branco)

# PORCENTAGEM INDIVIDUAL
listaritap = len(listarita) / total * 100
listaandradep = len(listaandrade) / total * 100
listasilvaniap = len(listasilvania) / total * 100
listalucianop = len(listaluciano) / total * 100
nulosp = len(nulos) / total * 100
brancop = len(branco) / total * 100

# DETERMINANDO O VENCEDOR
votos = {
    'RITA': len(listarita),
    'ANDRADE': len(listaandrade),
    'SILVANIA': len(listasilvania),
    'LUCIANO': len(listaluciano)
}
vencedor = max(votos, key=votos.get) if votos[max(votos, key=votos.get)] > 0 else "Nenhum"

resultado = (
    f'{multilinha}\n\n'
    f'        ⚖️  RESULTADO                       \n'
    f'        ⚖️  CANDIDATOS:                     \n'
    f'        ⚖️  RITA: {listaritap:.2f}%         \n'
    f'        ⚖️  ANDRADE: {listaandradep:.2f}%   \n'
    f'        ⚖️  SILVANIA: {listasilvaniap:.2f}% \n'
    f'        ⚖️  LUCIANO: {listalucianop:.2f}%   \n'
    f'        ⚖️  NULOS: {nulosp:.2f}%            \n'
    f'        ⚖️  VOTOS EM BRANCO: {brancop:.2f}% \n'
    f'\n O VENCEDOR FOI: {vencedor}\n'
    f'{multilinha}\n\n'
)

print(resultado)
