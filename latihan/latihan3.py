def bintang(n):
    for i in range(n-3):
        print(('*'*(1+2*i)).center(1+2*n))
    for x in range(n-3):
        print(('*'*(5-2*x)).center(1+2*n))
bintang(7)

