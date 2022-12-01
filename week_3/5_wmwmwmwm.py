def solution(n):
    answer = ''
    answer += '수박' * int(n/2)
    if n % 2 == 1:
        return answer + '수'
    else:
        return answer