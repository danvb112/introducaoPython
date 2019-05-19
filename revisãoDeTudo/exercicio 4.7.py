categoria = int( input( "Digite o núrmero da categoria que você deseja: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print ("Essa categoria não existe, por favor digite um número de 1 a 5!!") 
    preco = 0
print (" O preco da sua categoria é: ", preco)               

