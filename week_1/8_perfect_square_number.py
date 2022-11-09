def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        root = i ** 0.5
        if root % 1 == 0:
            answer -= i
        else:
            answer += i

    return answer