import math
from collections import defaultdict

# Given integer x, this returns the integer floor(sqrt(x)).
def sqrt(x: int) -> int:
    assert x >= 0
    i: int = 1
    while i * i <= x:
        i *= 2
    y: int = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y


def next_permutation(arr) -> bool:
    # Find non-increasing suffix
    i: int = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j: int = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True
# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def list_primality(n: int):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


# Returns all the prime numbers less than or equal to n, in ascending order.
# For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def list_primes(n: int):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]
def generate_primes(n: int):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            yield i
            for j in range(i * i, len(result), i):
                result[j] = False
    # return result
def pytha_trip(limit):
    triples = defaultdict(list)
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m ** 2 + n ** 2
                b = m ** 2 - n ** 2
                c = 2 * m * n
                if a < limit:
                    for k in range(1, limit // a + 1):
                        if k * a < limit:
                            triples[k * b].append(k * c)
                            triples[k * c].append(k * b)
    return triples

def get_roots(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return None, None
    # print(d)
    d = math.sqrt(d)
    # print(d)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2

def fermat_primality_test(n):
    if pow(4, n - 1, n) == 1 and pow(6, n - 1, n) == 1:
        return True
    return False
def is_prime(n):
    if not fermat_primality_test(n):
        return False

    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def get_prime_list(n):
    n += 1
    prime_check = [True] * n
    prime = []
    for i in range(2, n):
        if not prime_check[i]:
            continue
        prime.append(i)
        for j in range(i * i, n, i):
            prime_check[j] = False
    return prime


def next_permutation(arr) -> bool:
    # Find non-increasing suffix
    i: int = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j: int = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True