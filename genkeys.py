import random
from typing import List

from prime_numbers import get_prime_numbers


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def get_e_number(primes: List[int], euler: int):
    for _ in primes:
        e = random.choice(primes)
        if e % euler != 0 and euler % e != 0:
            return e
    return -1


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
    return e, n
