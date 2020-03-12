n_primo = 0
i = 3
n = 0
t = int(input(""))
while n <= t:
    n_primo = 0
    i = 3
    while True:
        if(n % 2 == 0):
            if(n == 2):
                print("%d é primo" % n)
                break
            else:
                #print("%d não é primo" % n)
                break
        while i < n:
            if(n % i == 0):
                n_primo += 1
                break
            i += 2
        if(n_primo == 0):
            if (n == 1):
                #print("%d não é primo" % n)
                break
            else:
                print("%d é primo" % n)
                break
        else:
            #print("%d não é primo" % n)
            break
    n += 1
