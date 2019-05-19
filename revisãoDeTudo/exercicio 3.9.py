print( "Digite seus dias, horas, minutos e segundos e saiba todo o seu resultado em segundos!")
d = int( input( "Digite seus dias: "))
h = int(input( "Digite suas horas: "))
m = int( input( "Digite seus minutos: "))
s = int( input( "Digite seus segundos: "))
horas = d *24
minutos =  (h + horas) * 60
segundos = ((minutos + m) * 60) + s
print(" Seu resultado em segundos é: ", segundos)