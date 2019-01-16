print( ' Saiba o valor de sua multa! ' )
velocidade = int(input( ' digite o valor da sua velocidade: '))
multa = 5 * (velocidade - 80)
if velocidade > 80:
    print ( 'Sua multa é de: ', multa) 
if velocidade <= 80:
    print (' Você não cometeu infração!')   
    