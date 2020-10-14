def genPrimes():
    primes = []  # primes generated so far
    last = 1  # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


k = genPrimes()

# for x in genPrimes(): # infinite loop, prints initte no. of prime numbers
#     print(x)

while True:
    print(f'next prime : {next(k)}')
    choice = input('    continue? y/n -> ')
    if choice.lower() == 'y':
        continue
    else:
        break
