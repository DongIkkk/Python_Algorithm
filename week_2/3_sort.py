def solution(n):
    n = sorted(str(n), reverse=True)
    answer = ''
    for i in n:
        answer += i
    return int(answer)