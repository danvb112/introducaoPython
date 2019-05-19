s = "um tigre, dois tigres, três tigres"
p = 0
while (p>-1):
    p = s.find("tigre", p)
    if p >= 0:
        print("posição: %d" % p)
    p = p + 1
