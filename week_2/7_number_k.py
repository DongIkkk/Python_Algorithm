def solution(array, commands):
    answer = []
    for i, j, k in commands:
        memory = array[i-1:j]
        memory.sort()
        answer.append(memory[k-1])
    return answer


# a = [1, 5, 2, 6, 3, 7, 4]
# b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(a, b))
