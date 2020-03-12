soma = 0
qtd = 0
while (True):
    numero = int(input("Digite um numero ou digite 0 para sair:"))
    if(numero == 0):
        break
    qtd = qtd+1
    soma = numero + soma
print("Quantidade de Numero Digitados:%d\nSoma:%d\nMédia:%.3f" %
      (qtd, soma, soma/qtd))
