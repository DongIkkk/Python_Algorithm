def solution(nums):
    select_total = len(nums) / 2
    set_nums = set(nums)
    vari = len(set_nums)

    if vari > select_total:
        return select_total
    else:
        return vari
