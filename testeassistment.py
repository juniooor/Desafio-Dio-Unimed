def SumPrimos(number):
    primos = []
    for a in range(1,number+1):
        l = []
        for i in range(1, a+1):
            (l).append(a % i)
        r = (l.count(0))
        if r == 2:
            primos.append(a)
    return sum(primos)

