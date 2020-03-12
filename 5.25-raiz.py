n = float(input(""))
b = 2
pb = 0
p = (b+(n/b))
while abs(n-pb) > 0.0001:
    b = p
    p = (b+(n/b))/2
    pb = pow(p, 2)
print("%.2f" % b)
