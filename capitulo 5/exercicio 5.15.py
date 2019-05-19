print( " Bem vindo a máquina de compras!")
print( "Temos os segintes produtos: ")
print("produto 1 = preço R$ 0.50 ")
print("produto 2 = preço R$ 1.00 ")
print("produto 3 = preço R$ 4.00 ")
print("produto 5 = preço R$ 7.00 ")
print("produto 9 = preço R$ 8.00 ") 
total = 0
while True:
    categoria = int (input(" Digite o código do produto ou 0 pata sair: "))
    if categoria == 0:
        break
    elif categoria > 9:
        print(" codigo inválido!")
        continue
    elif categoria == 4 or categoria == 6 or categoria == 7 or categoria == 8:
        print(" codigo inválido!")
        continue
    quantidade = int (input("digite a quantidade que você deseja dessa categoria:  "))
    if categoria == 1:
        preco = 0.50
    elif categoria == 2:
        preco = 1
    elif categoria == 3:
        preco = 4 
    elif categoria == 5:
        preco = 7
    elif categoria == 9:
        preco = 8 
    total = total + (preco * quantidade)
print ("Seu total de compras foi: %5.2f" %(total))
