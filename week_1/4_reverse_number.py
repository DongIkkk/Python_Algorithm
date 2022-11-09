def solution(n):
    answer = list(map(int, (i for i in str(n))))
    answer.reverse()
    return answer
