print (" Saiba o valor da prestração do empréstimo para sua casa!!")
print (" O seu empréstimo só será liberado se a parcela for maior ou igual a 30% do seu salário")
valorDaCasa = int( input( "Primeiro digite o valor da casa aqui: "))
salario = float( input( "agora digite o valor do seu salário: "))
anos = int( input( "Agora digite a quantidade de anos que você planeja pagar a casa: "))
meses = anos * 12
prestacao = valorDaCasa / meses
print ("relatório: \n valor da casa: %d \n seu salário: %6.2f \n seus meses a pagar: %d \n sua prestação: %d " % ( valorDaCasa , salario , meses , prestacao ))
if prestacao <= 0.3 * salario:
    print (" Seu emprestimo foi liberado e o valor da sua prestação vai ser de: R$%6.2f "  % ( prestacao ) )
elif prestacao > 0.3 * salario:
    print (' seu emprestimo não foi liberado, por favor receba um aumento de salário!')
    