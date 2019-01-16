print( ' Saiba quanto vai ser o seu aumento de salário!')
salario = int( input( "primeiro digite o seu salário aqui: "))
if salario > 1250:
    aumento = (salario * 0.10)
    novoSalario = salario + aumento
if salario <= 1250:
    aumento = (salario * 0.15)
    novoSalario = salario + aumento
print ( ' O seu aumento é de: R$' , aumento)
print ( ' E o seu novo salário é: R$' , novoSalario)