print(" Saiba quanto você irá ganhar de juros ao depositar na sua poupança")
deposito = int(input( "Digite o valor do seu deposito aqui: "))
taxaDeJuros = float( input( "Digite sua taxa de juros aqui: "))
conta = deposito + (deposito * taxaDeJuros /100)
x = 1
while x <= 24:
    resultado = conta + (conta * 10 / 100) 
    total = resultado
    print(" mês %d = %5.2f" %(x , total))
    x = x + 1
