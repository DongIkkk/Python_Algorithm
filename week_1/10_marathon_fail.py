# 1. 시간초과
# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     answer = participant.pop()
#     return answer

# 2.시간초과
# def solution(participant, completion):
#     for i in participant:
#         if i in completion:
#             completion.remove(i)
#         else:
#             return i

# 3. 해시 - 딕셔너리로해보기
def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for j in completion:
        hash[j] -= 1

    # value값으로 key 찾기
    for k, v in hash.items():
        if v == 1:
            return k


p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
print(solution(p, c))
