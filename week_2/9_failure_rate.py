def solution(N, stages):
    fail_dic = {}
    total = len(stages)
    for i in range(1, N+1):
        if total == 0:
            fail_dic[i] = 0
        else:
            fail_dic[i] = stages.count(i) / total

        total -= stages.count(i)

    sorted_fail_dic = sorted(fail_dic, key=lambda x: fail_dic[x], reverse=True)

    return sorted_fail_dic
