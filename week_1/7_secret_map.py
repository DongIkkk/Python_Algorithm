def dec_to_bin(l, num):
    memory = ''
    for _ in range(l):
        if num >= 2**(l-1):
            num -= 2**(l-1)
            l -= 1
            memory += '1'
        else:
            l -= 1
            memory += '0'
    return memory

# format, bin, zfill 활용해보기


def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []

    for i in arr1:
        new_arr1.append(dec_to_bin(n, i))

    for j in arr2:
        new_arr2.append(dec_to_bin(n, j))

# --------------------------
#     arr1 = [9, 20, 28, 18, 11]
#     arr2 = [30, 1, 21, 17, 28]
#     n = 5
#     for i in range(len(arr1)):
#         bin1 = bin(arr1[i])[2:].zfill(n)
#         bin2 = bin(arr2[i])[2:].zfill(n)
#     print(bin1)
#     print(bin2)
# -------------------------

    result_arr = []

    for k in range(n):
        a = new_arr1[k]
        b = new_arr2[k]
        a = str(a)
        b = str(b)
        c = ''

        for l in range(len(a)):

            if a[l]=='0' and b[l]=='0':
                c += ' '
            else:
                c += '#'

        result_arr.append(c)

    return result_arr
