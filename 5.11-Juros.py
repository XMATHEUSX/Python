deposito_inicial = float(input("Depósito incial:R$"))
juros = float(input("Taxa de juros:"))
mensal = float(input("Valor Despositado mensalmente:"))
mes = 0
deposito = deposito_inicial
while (mes < 24):
    mes = mes+1
    deposito = mensal+deposito + deposito/100*juros
    print("%d°Mes : R$%5.2f" % (mes, deposito))
print("Ganho total com juros:R$%5.2f" % (deposito-deposito_inicial))
