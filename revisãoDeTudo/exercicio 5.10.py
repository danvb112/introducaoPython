pontos = 0
questao = 1 
while questao <= 3:
    resposta = input ("Digite a resposta da questão %d: " %(questao))
    if questao == 1 and resposta == "A" or "a":
        pontos = pontos + 1
    if questao == 2 and resposta == "B" or "b":
        pontos = pontos + 1 
    if questao == 3 and resposta == "C" or "c":
        pontos = pontos + 1 
    questao = questao + 1
print ("O aluno fez %d pontos" %(pontos))