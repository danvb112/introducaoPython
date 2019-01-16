print ( 'Bem vindo ao transformador de dias, horas e segundos em segundos!')
print ( 'Primeiro insira sua quantidade de dias:')
dias = int(input())
print ( 'Agora insira sua quantidade de horas:')
horas = int(input())
print ( 'E por ultimo insira sua quantidade de segundos:' )
segundos = int(input())
totalEmSegundos = dias * 86400 + horas * 3600 + segundos
print ( 'O resultado em segundos é:', totalEmSegundos)