print(" Saiba quanto você irá pagar pela energia!!")
kWh = int(input("Digite a quantidade de kWh consumidas: "))
tipoInstalação = input(" Digite o tipo da sua intalação sendo: \n residencial (R) \n Comercial (C) \n industrial (I) \n")
if tipoInstalação == "R" or "r":
    if kWh <= 500:
        preco = kWh * 0.4
    elif kWh > 500:
        preco = kWh * 0.65
if tipoInstalação == "C" or "c":
    if kWh <= 1000:
        preco = kWh * 0.55
    elif kWh > 1000:
        preco = kWh * 0.6
if tipoInstalação == "I" or "i":
    if kWh <= 5000:
        preco = kWh * 0.55
    elif kWh > 5000:
        preco = kWh * 0.6
print ("o preco que você irá pagar pela energia será de: R$%4.2f" %(preco))                                    