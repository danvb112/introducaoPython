print("Digite o preço de uma mercadoria e seu desconto para saber quanto você irá pagar!")
mercadoria = int( input( "Digite o preço da mercadoria aqui: "))
percentual = int (input(" Digite o percentual do desconto aqui: "))
desconto = mercadoria * percentual /100
precoFinal = mercadoria - desconto 
print( "Você vai pagar: " , precoFinal)