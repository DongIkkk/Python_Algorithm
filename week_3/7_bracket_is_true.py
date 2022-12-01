def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count == -1:
            return False

    if count == 0:
        return True
    else:
        return False


