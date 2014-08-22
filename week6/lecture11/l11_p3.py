def genPrimes():
    primes = []
    x = 1
    while True:
        x += 1
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield x

g = genPrimes()
for i in range(7):
    print g.next()
