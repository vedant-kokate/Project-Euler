import itertools
import time
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6

    return True
def compute():
    TARGET = 1/10
    numprimes = 0
    for n in itertools.count(1, 2):
        for i in range(1,4):
            if isPrime(n * n - i * (n - 1)):
                numprimes += 1
        if n > 1 and numprimes/(n * 2 - 1) < TARGET:
            return n


if __name__ == "__main__":
    st=time.time()
    print(compute())
    print(time.time()-st,'s') 
