valor1 = float(input('Digite o primeiro valor:'))
valor2 = float(input('Digite o segundo valor:'))
operacao = input('escolha a operação:soma, subtração, multiplicação, divisão').upper().strip()
operacao = operacao.replace("Ã","A").replace("Ç","C").replace(',','.')
resultado = ''
resto = ''

#OPERAÇÕES
if operacao == 'SOMA':
    valor1 + valor2 = resultado
if operacao == 'SUBTRACAO':
    valor1 - valor2 = resultado
if operacao == 'MULTIPLICACAO':
    valor1 * valor2 = resultado
if operacao == 'DIVISAO':
    valor1 / valor2 = resultado
    valor1 % valor2 = resto

#PAR OU IMPAR
parouimpar = ''

if  resultado % 2 == 0:
    parouimpar = 'PAR'
else:
    parouimpar = 'IMPAR'

#POSITIVO OU NEGATIVO OU NEUTRO
positivoounegativo = ''

if resultado > 0:
    positivoounegativo = 'POSITIVO'
elif resultado < 0:
    positivoounegativo = 'NEGATIVO'
else:
    positivoounegativo = 'NEUTRO'

#INTEIRO OU DECIMAL
inteirooudecimal = ''

#dividir ele mesmo formato float por ele no formato int
if type(resultado) == float:
    inteirooudecimal = 'DECIMAL'
elif type(resultado) == int:
    inteirooudecimal == 'INTEIRO'

#RETORNAR A RESPOSTA 
 
if operacao == 'DIVISAO':
    print(f'Você escolheu a operação {operacao} que resultou em {resultado} que é {parouimpar}, {positivoounegativo}, {inteirooudecimal} e restou {resto}')
else:
    print(f'Você escolheu a operação {operacao} que resultou em {resultado} que é {parouimpar}, {positivoounegativo} e {inteirooudecimal}')


      
 
    



