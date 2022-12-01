def solution(s):
    num = len(s)
    slicing_num = int(num/2)
    if num % 2 == 1:
        return s[slicing_num]
    else:
        return s[slicing_num-1:slicing_num+1]