def solution(n, lost, reserve):
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    lost2 = lost.copy()
    reserve2 = reserve.copy()

    if n in reserve:
        for i in reserve:
            if (int(i) - 1) in lost:
                lost.remove(int(i) - 1)
            elif (int(i) + 1) in lost:
                lost.remove(int(i) + 1)
        answer = n - len(lost)

    elif 1 in reserve:
        for i in reserve:
            if (int(i) + 1) in lost:
                lost.remove(int(i) + 1)
            elif (int(i) - 1) in lost:
                lost.remove(int(i) - 1)
        answer = n - len(lost)

    else:
        for i in reserve:
            if (int(i) - 1) in lost:
                lost.remove(int(i) - 1)
            elif (int(i) + 1) in lost:
                lost.remove(int(i) + 1)
        result = n - len(lost)
        for i in reserve2:
            if (int(i) + 1) in lost2:
                lost2.remove(int(i) + 1)
            elif (int(i) - 1) in lost:
                lost2.remove(int(i) - 1)
        result2 = n - len(lost)

        answer = max(result, result2)

    answer = n - len(lost)

    return answer
