for i in range(2,5000):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
