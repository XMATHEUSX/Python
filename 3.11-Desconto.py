preco = float(input("Preço da mercadoria:"))
desconto = float(input("Desconto:"))
preco_com_desconto = preco-(preco/100*desconto)
print("desconto de R$%.2f\nPreço do produto com desconto R$%.2f" %
      (preco/100*desconto, preco_com_desconto))
