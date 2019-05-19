L = [15,7,24,29]
p = int(input("Digite o valor a procurar: "))
achpu = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x = x + 1
if achou:
    print("%d achado na posição %d" %(p,x))
else:
    print("%d não encontrado" %p)
