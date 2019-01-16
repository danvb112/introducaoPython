print ( ' Saiba quantos dias de vida um fumante perde!!')
cigarros = int(input(' Digite o numero de cigarros fumados por dia: '))
anos = int(input(' Agora digite a qantidade de anos fumados: '))
dias = anos * 365
diasCigarro = cigarros * 10 / 1440
diasPerdidos = dias * diasCigarro
print ( ' O numero de dias perdidos por esse fumante foi: ', diasPerdidos)