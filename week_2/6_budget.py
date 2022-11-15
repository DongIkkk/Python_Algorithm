def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if budget >= i:
            budget -= i
        else:
            return answer
        answer += 1

    return answer