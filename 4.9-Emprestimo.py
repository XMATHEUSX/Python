valor_casa = float(input("Valor da casa:"))
salario = float(input("Salário:"))
anos = int(input("Anos para pagar:"))
mensalidade = valor_casa/(anos*12)
if (mensalidade <= ((salario/100)*30)):
    print("Empréstimo Aprovado")
else:
    print("Empréstimo Reprovado")
