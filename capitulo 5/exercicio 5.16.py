valor = float(input("Digite o valor a pagar: "))
cedulas = 0
moeda = 0
moedaAtual = 0.50
atual = 100
apagar = valor 
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print ("%d células de R$%d" %( cedulas, atual))
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0 
    if atual <= moedaAtual:
        apagar -= moedaAtual
        moeda += 1
    else:
        print ("%d moedas de R$%2.2f" %( moeda, moedaAtual))
        if atual == 0:
            break
        if moedaAtual == 0.50:
            moedaAtual = 0.10
        if moedaAtual == 0.10:
            moedaAtual = 0.05
        if moedaAtual == 0.05:
            moedaAtual = 0.01
        moeda = 0