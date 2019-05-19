print ("Digite dois número e a operação que deseja fazer com eles!!")
primeiro = int( input(" Digite o primeiro número: "))
segundo = int( input(" Digite o segundo número: "))
operação = input( "Digite a operação sendo: \n soma (+) \n subtração (-) \n multiplicação (*) \n divisão (/) \n ")
if operação == "+":
    resultado = primeiro + segundo
elif operação == "-":
    resultado = primeiro - segundo
elif operação == "*":
    resultado = primeiro * segundo
elif operação == "/":
    resultado = primeiro / segundo
print ("O resultado da sua operação é: " ,resultado)
