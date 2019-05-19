print (" Saiba quanto você irpa receber de aumento!!")
salario = int( input(" Digite o valor do seu salário aqui: "))
if salario > 1250:
    novoSalario1 = salario + (salario * 10/100)
    print ( "Seu novo salário é: %d" % ( novoSalario1 ))
if salario < 1250:
    novoSalario2 = salario + (salario * 15/100)
    print ( "Seu novo salário é: %d" % ( novoSalario2 ))
if salario == 1250:
    print (" Não houve aumento no seu salário!")    
    

