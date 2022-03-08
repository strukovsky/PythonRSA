from typing import List


def is_prime(number: int) -> bool:
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def get_prime_numbers(upper_limit: int) -> List[int]:
    result: List[int] = []
    for i in range(2, upper_limit):
        if is_prime(i):
            result.append(i)
    return result
