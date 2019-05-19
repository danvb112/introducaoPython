x = 1
soma = 0 
while True:
    n = int(input("Digite um número ou 0 para sair: "))
    soma = soma + n
    if n == 0:
        break
    x = x + 1 
print ("números digitados: %d \n soma: %d \n média: %5.2f" %( x , soma , (soma / x)))
