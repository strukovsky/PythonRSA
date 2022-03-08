import random
from typing import List

from prime_numbers import get_prime_numbers


class PublicKey:

    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n

    def __str__(self):
        return f"Public key e: {self.e} n: {self.n}"

    def __repr__(self):
        return str(self)


class PrivateKey:

    def __init__(self, d, n):
        self.d = d
        self.n = n

    def __str__(self):
        return f"Private key d: {self.d} n: {self.n}"

    def __repr__(self):
        return str(self)


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def get_e_number(primes: List[int], euler: int):
    for _ in primes:
        e = random.choice(primes)
        if e % euler != 0 and euler % e != 0:
            return e
    return -1


def get_d_number(euler: int, e: int) -> int:
    k = 0
    dummy_d = 1
    d = 0
    while dummy_d != d:
        k += 1
        dummy_d = (k * euler + 1) / e
        d = (k * euler + 1) // e
    return d


def gen_keys(upper_limit_for_primes: int = 10000):
    primes = get_prime_numbers(upper_limit_for_primes)
    [p, q] = random.choices(primes, k=2)
    euler = euler_function(p, q)
    n = p * q
    primes_less_than_n = []
    for prime in primes:
        if prime < n:
            primes_less_than_n.append(prime)
    e = get_e_number(primes_less_than_n, euler)
    d = get_d_number(euler, e)
    return PublicKey(e, n), PrivateKey(d, n)
