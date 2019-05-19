print( " Saiba quanto você irá pagar pelo seu carro alugado!")
km = int( input( "Digite a quantidade de Km percorridos com o carro: "))
dias = int (input( "Digite a quantidade de dias que utilizou o carro: "))
precoDia = dias * 60
precoKm = km * 0.15
preçoFinal = precoDia + precoKm
print( "O valor a ser pago é: ", preçoFinal)