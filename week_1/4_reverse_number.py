def solution(n):
    answer = list(map(int, (i for i in str(n))))
    answer.reverse()
    return answer
# reverse는 리턴이나 리스트생성 줄에선 안되는듯
