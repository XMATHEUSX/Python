total = 0
compra = 0
while(True):
    cod = int(input("Código Do Produto:"))
    if(cod == 0):
        break
    qtd = int(input("Quantidade:"))
    if(cod == 1):
        compra = qtd*0.50
    elif(cod == 2):
        compra = qtd*1
    elif(cod == 3):
        compra = qtd*4
    elif(cod == 5):
        compra = qtd*7
    elif(cod == 9):
        compra = qtd*8
    else:
        print("Código inválido")
    total = compra+total
print("Valor da Total da Compra:R$", total)
