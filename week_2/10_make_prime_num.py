from itertools import combinations


def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def solution(nums):
    nCr = list(combinations(nums, 3))
    sum_list = []
    for i in nCr:
        memory = sum(i)
        sum_list.append(memory)

    count = 0
    for j in sum_list:
        if is_prime(j):
            count += 1

    return count
