print (" calcule o aumento do seu salário aqui!!")
print ( ' Primeiro digite o valor do seu salário:')
salario = int(input())
print ( ' Agora digite a porcentagem do aumento: ')
porcentagemAumento = float( input())
novoSalario = salario + (salario * porcentagemAumento / 100)
aumento = salario * porcentagemAumento / 100
print ( 'O seu aumento e novo salario são:' , aumento , novoSalario)
