from random import randrange

multilinha = '=' * 50

titulo = (
    f'{multilinha}\n\n'
    f'        🌟       MENU DE FRUTAS       🌟\n\n'
    f'{multilinha}\n\n'
)

frutas = [
    "maçã", "banana", "uva", "pêra", 
    "manga", "coco", "melancia", "mamão",
    "laranja", "abacaxi", "kiwi", "ameixa"
]

menu_frutas = '\n'.join(
    f'{i + 1:>2}. 🟡 {fruta.title()}' for i, fruta in enumerate(frutas)
)

menu = (
    f'{titulo}'
    f'{menu_frutas}\n\n'
    f'{multilinha}'
)

print(menu)

res = int(input('OPÇÕES:\n FORMA TRADICIONAL( 1 ) -> ESCOLHA VOCÊ MESMO AS FRUTAS\n MODO SURPRESA( 2 ) -> SÃO ESCOLHIDOS ALEATORIAMENTE AS FRUTAS\n RESPONDA 1 PARA MODO TRADICIONAL E 2 PARA MODO SURPRESA\n').strip())
pedido = []

if res == 1:
    print(menu_frutas)
    quantidade = int(input('\nENTÃO DIGA A QUANTIDADE DE FRUTAS DESEJADAS:').strip())
    for i in range(1,quantidade+1):
        ingredientes = int(input(f'{multilinha}\nINDIQUE PELO NUMERO AO LADO DA FRUTA: ').strip())
        pedido.append(frutas[ingredientes-1].upper())
        print(f'\n{frutas[ingredientes-1].upper()} FOI ADICIONADO')
    
    print(f'\nSEU PEDIDO FOI CONCLUIDO! SUA SALADA DE FRUTA COM {pedido} JÁ VAI SER ENTREGUE\n')
    
elif res == 2:
    quantidade = int(input('\nENTÃO DIGA A QUANTIDADE DE FRUTAS DESEJADAS:').strip())
    for i in range(1,quantidade+1):
       ingredientes = randrange(1,12)
       pedido.append(frutas[ingredientes-1].upper())
    
    print(f'\nSEU PEDIDO FOI CONCLUIDO! SUA SALADA DE FRUTA COM {pedido} JÁ VAI SER ENTREGUE\n')

else:
    while res != 1 and res != 2:
        print('NÃO ENTENDI, LEIA AS REGRAS E FALE NOVAMENTE')
        res = int(input('OPÇÕES:\n FORMA TRADICIONAL( 1 ) -> ESCOLHA VOCÊ MESMO AS FRUTAS\n MODO SURPRESA( 2 ) -> SÃO ESCOLHIDOS ALEATORIAMENTE AS FRUTAS\n RESPONDA 1 PARA MODO TRADICIONAL E 2 PARA MODO SURPRESA\n').strip())
    
    if res == 1:
        print(menu_frutas)
        quantidade = int(input('\nENTÃO DIGA A QUANTIDADE DE FRUTAS DESEJADAS:').strip())
        for i in range(1, quantidade + 1):
            ingredientes = int(input(f'{multilinha}\nINDIQUE PELO NUMERO AO LADO DA FRUTA: ').strip())
            pedido.append(frutas[ingredientes - 1].upper())
            print(f'\n{frutas[ingredientes - 1].upper()} FOI ADICIONADO')
        
        print(f'\nSEU PEDIDO FOI CONCLUIDO! SUA SALADA DE FRUTA COM {pedido} JÁ VAI SER ENTREGUE\n')
    
    elif res == 2:
        quantidade = int(input('\nENTÃO DIGA A QUANTIDADE DE FRUTAS DESEJADAS:').strip())
        for i in range(1, quantidade + 1):
            ingredientes = randrange(1, 12)  
            pedido.append(frutas[ingredientes - 1].upper())
        
        print(f'\nSEU PEDIDO FOI CONCLUIDO! SUA SALADA DE FRUTA COM {pedido} JÁ VAI SER ENTREGUE\n')


       

       



      
      

         

