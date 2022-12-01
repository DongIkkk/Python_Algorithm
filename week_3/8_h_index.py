def solution(citations):
    citations.sort(reverse=True)
    count = 0
    for i in citations:
        count += 1
        if count >= i:
            return i
    return 0


print(solution([0,1,2,3,4]))