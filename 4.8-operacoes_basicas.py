A = float(input("Primeiro número"))
B = float(input("Segundo  número:"))
operacao = input(
    "Digite o respectivo simbolo da opreção que deseja realizar\nSoma(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)\n")
if(operacao == "+"):
    print(A+B)
elif(operacao == "-"):
    print(A-B)
elif(operacao == "*"):
    print(A*B)
elif(operacao == "/"):
    if(B == 0):
        print("Não é possivel dividir por zero")
    else:
        print(A/B)
