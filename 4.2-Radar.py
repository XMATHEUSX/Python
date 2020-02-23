velocidade = int(input("Velocidade do Carro:"))
if (velocidade > 80):
    print("MULTA!!!\nValor R$%d" % ((velocidade-80)*5))
