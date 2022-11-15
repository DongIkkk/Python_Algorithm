def solution(s):
    if s[0].isdigit():
        answer = int(s)
    elif s[0] == '-':
        answer = 0 - int(s[1:])
    else:
        answer = int(s[1:])
    return answer

# answer = int(s)