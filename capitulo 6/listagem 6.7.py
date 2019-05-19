numero = [0,0,0,0,0]
x = 0
while x < 5:
    numero[x] = int(input("Número %d: "%(x + 1)))
    x += 1
while True:
    escolhido = int(input("que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print("Você escolheu o número: %d" %(numero[escolhido - 1]))
