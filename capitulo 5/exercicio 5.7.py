inicio = int(input(" Digite o inicio da tabuada: "))
fim  = int(input(" Digite o final da tabuada: "))
x = inicio * 2
n = inicio
while n <= fim:
    print (" 2x%d = %d" %( n , x))
    n = n + 1
    x = x + 2