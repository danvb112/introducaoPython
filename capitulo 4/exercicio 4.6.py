print( "Saiba o preço de sua passagem aqui!!")
distancia = float( input( 'Digite quantos Km você deseja percorrer: '))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print ( " o valor de sua passagem é: R$%5.2f" % (passagem))    
