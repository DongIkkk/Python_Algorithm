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
# 해시테이블 딕셔너리
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

# 다른방법 collections.Counter   import 해야 쓸수있음 주의
# import collections
# def solution(participant, completion):
# answer = collections.Counter(participant) - collections.Counter(completion)
# return list(answer.keys())[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# 해시문항 풀어보기
# https://www.acmicpc.net/problemset?sort=ac_desc&algo=136


# 입출력예시
p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
print(solution(p, c))
