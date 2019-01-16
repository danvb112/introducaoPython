print (' Bem vindo ao calculador de descontos!!')
print ( ' insira o preço de uma mercadoria e do desconto e saiba quanto vai pagar!!')
print ( " primeiro insira o preço da mercadoria:")
mercadoria = int(input())
print ( ' agora insira o percentual do desconto:')
percentualDoDesconto = float(input())
desconto = mercadoria * percentualDoDesconto /100
valorAserPago = mercadoria - desconto
print ( ' o seu desconto e valor a ser pago na mercadoria são respectivamente:', desconto , valorAserPago)