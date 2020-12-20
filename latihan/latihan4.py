def shuffleString(x, n):
    import random

    for i in range(n):
        a = list(random.sample(x,len(x)))
        b = ''.join(a)
        c = b.split()
        print(c)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 3)
