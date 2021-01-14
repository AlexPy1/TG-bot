import itertools



   # d = 2
    #if p == 2:
     #   yield p
    #else:
     #   while p % d != 0:
      #      d += 1

       #     if d == p:
        #        yield p
def primes():
    for p in range(2,100000):
        d = 2
        if p == 2:
            yield p
        else:
            while p % d != 0:
                d += 1

                if d == p:
                    yield p

print(list(itertools.takewhile(lambda x : x <= 100000, primes())))

