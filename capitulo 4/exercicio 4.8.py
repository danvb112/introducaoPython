print (" Digite dois numero e escolha a operação matematica!")
primeiroNumero = int( input( "Digite o primeiro número: " ))
segundoNumero = int( input( "Digite o segundo número: "))
operacao = input( "Agora digite a operação desejada: \n + = soma \n - = subtração \n * = multiplicação \n / = divisão \n")
if operacao == "+":
    soma = primeiroNumero + segundoNumero
    print ('A sua soma é: ', soma)
elif operacao == "-":
    subtracao = primeiroNumero - segundoNumero
    print (" A sua subtração é:", subtracao)
elif operacao == "*":
    multiplicacao = primeiroNumero * segundoNumero
    print (" A sua multiplicação é:", multiplicacao)
elif operacao == "/":
    divisao = primeiroNumero / segundoNumero
    print (" A sua divisão é:", divisao)        

