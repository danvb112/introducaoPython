print (" Saiba quanto você irá pagar pela sua viagem!")
distancia = int( input( "Digite a distancia a ser percorrida me Km: "))
if distancia <= 200:
    precoDaPassagem1 = distancia * 0.5
    print (" O preço de sua passagem é: R$%d" % (precoDaPassagem1))
else:
    if distancia > 200:
        precoDaPassagem2 = distancia * 0.45
        print (" O preço da sua passagem é: R$%d" % ( precoDaPassagem2))    