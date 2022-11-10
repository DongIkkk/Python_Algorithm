def solution(s):
    base = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ''
    memory = ''

    for i in s:
        if i.isdigit():
            answer += i
        else:
            memory += i

        if memory in base:
            answer += base[memory]
            memory = ''

    return int(answer)

# in, replace, index를 활용해보기

# arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#
# arr2 = 'zeroonehello'
#
# inarr = 'zero' in arr
# inarr2 = 'zero' in arr2
#
# print(inarr, inarr2)