valorCasa = float (input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
anosPagar = int(input("em quantos anos você deseja pagar: "))
meses = anosPagar * 12
prestação = valorCasa / meses
if prestação > salario * 0.3:
    print ("O emprestimo não foi aprovado")
elif prestação < salario*0.3:
    print ("O emprestimo foi aprovado") 