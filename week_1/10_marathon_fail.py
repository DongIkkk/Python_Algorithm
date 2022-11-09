# 1. 시간초과
# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     answer = participant.pop()
#     return answer

# 2.시간초과
def solution(participant, completion):
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            return i
