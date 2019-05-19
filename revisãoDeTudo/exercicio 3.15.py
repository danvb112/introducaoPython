print( "Saiba quantos dias de vida um fumante perde!!")
cigarrosDias = int( input( "Digite quantos cigarros o fumante usa por dia: "))
anos = int( input( "Digite quantos anos o fumante fuma: "))
dias = anos * 365
totalCigarros = cigarrosDias * dias
diasPerdidos = dias - (totalCigarros * 10 / 1440) 
print( " Em %d anos o fumante perdeu %d dias de vida" % (anos , diasPerdidos))
