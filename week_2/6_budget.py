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



# sorted
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
print("sorted data: ", sorted(arr))
# arr = sorted(arr)
print("input data: ", arr)
# sort()
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
arr.sort()
print("input data: ", arr)