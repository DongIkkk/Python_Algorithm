def collatz(count, num):
    if count == 500:
        return -1
    elif num == 1:
        return count
    elif num % 2 == 0:
        count += 1
        num1 = num/2
        return collatz(count, num1)
    else:
        count += 1
        num2 = (num * 3) + 1
        return collatz(count, num2)


def solution(num):
    return collatz(0, num)
