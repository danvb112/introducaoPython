print( ' Saiba quanto você deve pagar pelo aluguel de um carro!! ')
dias = int(input( 'primeiro digite a quantidade de dias que você usou o carro: '))
km = int(input( ' Agora digite a qantidade de Km que você rodou com o carro: '))
preco = dias * 60 + km * 15 / 100
print (' o valor que você deve pagar é: ', preco)