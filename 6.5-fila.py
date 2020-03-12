import sys
utlimo = 5
fila1 = list(range(1, utlimo+1))
fila2 = []
operacao1 = []
while True:
    print("\n Existem %d cliente na fila 1 e %d cleinte na fila 2" %
          (len(fila1), len(fila2)))
    print("Fila 1 atual:", fila1, "\nFila2 atual:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para Realizar o atendimento. S para sair")
    operacao = input("operação(F,A ou S)")
    operacao = operacao.replace("", " ").strip().split(" ")
    operacao1.extend(operacao)
    while len(operacao1) >= 1:
        if operacao1[0] == "A":
            if(len(fila1)) > 0:
                atendido = fila1.pop(0)
                del operacao1[0]
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila Vazia! Ninguém para atender.")
                break
        elif operacao1[0] == "B":
            if(len(fila2)) > 0:
                atendido = fila2.pop(0)
                del operacao1[0]
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila Vazia! Ninguém para atender.")
                break
        elif operacao1[0] == "F":
            utlimo += 1
            fila1.append(utlimo)
            del operacao1[0]
        elif operacao1[0] == "G":
            utlimo += 1
            fila2.append(utlimo)
            del operacao1[0]
        elif operacao1[0] == "S":
            del operacao1[0]
            sys.exit()
        else:
            print("Operação inválida! Digite apenas F,A ou S!")
            break
