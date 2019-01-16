print ( ' Digite tês números e saiba o seu maior e menor!')
a = int( input('Digite o primeiro número: '))
b = int( input( 'Digite o segundo número: '))
c = int( input( 'Digite o terceiro número: '))
if a > b  > c:
    maiorNumero = a
    menorNumero = c
if a > c > b:
    maiorNumero = a
    menorNumero = b
if b > a > c:
    maiorNumero = b
    menorNumero = c
if b > c > a:
    maiorNumero = b
    menorNumero = a
if c > a > b:
    maiorNumero = c
    menorNumero = b
if c > b > a:
    maiorNumero = c
    menorNumero = a
print (' O seu maior número é: ', maiorNumero)
print ( 'O seu menor número é: ', menorNumero)