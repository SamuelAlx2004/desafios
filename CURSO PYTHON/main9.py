contador = None
mediaquantidade = None
valor = None
while valor != -273:
    valor = float(input('Informe o valor da temperatura:'))
    if contador is None and mediaquantidade is None:
        contador = 0
        mediaquantidade = 0
    contador += valor
    mediaquantidade += 1
    media = contador / mediaquantidade
    print(F'--------------------------------------------------------\nUltimo valor retornado foi {valor}\n e a media atual é {media}\n--------------------------------------------------------')
    if valor == -273:
        print('\nCODIGO ENCERRADO!\n')

