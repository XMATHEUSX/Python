n = input("Digite um numero:")
if(n == n[::-1]):
    print("%s é um palíndromo" % n)
else:
    print("%s Não é um palíndromo" % n)
