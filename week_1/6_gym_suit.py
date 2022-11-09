def solution(n, lost, reserve):
    # 이렇게 지우면 안됨 index 밀린다
    # for i in lost:
    #     if i in reserve:
    #         lost.remove(i)
    #         reserve.remove(i)
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]

    lost2 = new_lost.copy()
    reserve2 = new_reserve.copy()

    for i in new_reserve:
        if (i - 1) in new_lost:
            new_lost.remove(i - 1)
        elif (i + 1) in new_lost:
            new_lost.remove(i + 1)
    result = n - len(new_lost)
    for i in reserve2:
        if (i + 1) in lost2:
            lost2.remove(i + 1)
        elif (i - 1) in lost2:
            lost2.remove(i - 1)
    result2 = n - len(lost2)

    answer = max(result, result2)

    return answer
