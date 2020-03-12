while True:
    valor = float(input("Digite o valor a pagar:"))
    cedulas = 0
    moedas = 0
    atual = 100
    apagar = valor
    if(valor == 0):
        break
    while True:
        if apagar < 0.01:
            apagar = round(apagar, 2)
        if atual <= apagar:
            apagar = round(apagar, 3) - round(atual, 2)
            cedulas += 1
        else:
            if atual < 1:
                print("%d Moedas de R$%.2f " % (cedulas, atual))
            else:
                print("%d cedulas de R$%.2f" % (cedulas, atual))
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
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            cedulas = 0
