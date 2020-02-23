materia1 = int(input("Digite a nota de matemática:"))
materia2 = int(input("Digite a nota de Português:"))
materia3 = int(input("Digite a nota de Ciências:"))
matematica = materia1 > 7
portugues = materia2 > 7
ciencia = materia3 > 7
aprovado = matematica and portugues and ciencia
print("Aprovação:", aprovado)
