def solution(dartResult):
    count = 1
    x, y, z = 1, 1, 1
    slash = ['S', 'D', 'T', '*', '#']
    ten_check = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if ten_check == 1:
                ten_check = 0
                continue
            else:
                if (dartResult[i+1]) == '0':
                    if count == 1:
                        x = int(x) * 10
                        ten_check = 1
                    elif count == 2:
                        y = int(y) * 10
                        ten_check = 1
                    else:
                        z = int(z) * 10
                        ten_check = 1
                else:
                    if count == 1:
                        x = int(x) * int(dartResult[i])
                    elif count == 2:
                        y = int(y) * int(dartResult[i])
                    else:
                        z = int(z) * int(dartResult[i])
                
                    
        elif dartResult[i] in slash:
            if dartResult[i] == 'S':
                if count == 1:
                    x = int(x) ** 1
                    if dartResult[i+1].isdigit():
                        count+=1
                elif count == 2:
                    y = int(y) ** 1
                    if dartResult[i+1].isdigit():
                        count+=1
                else:
                    z = int(z) ** 1
            elif dartResult[i] == 'D':
                if count == 1:
                    x = int(x) ** 2
                    if dartResult[i+1].isdigit():
                        count+=1
                elif count == 2:
                    y = int(y) ** 2
                    if dartResult[i+1].isdigit():
                        count+=1
                else:
                    z = int(z) ** 2
            elif dartResult[i] == 'T':
                if count == 1:
                    x = int(x) ** 3
                    if dartResult[i+1].isdigit():
                        count+=1
                elif count == 2:
                    y = int(y) ** 3
                    if dartResult[i+1].isdigit():
                        count+=1
                else:
                    z = int(z) ** 3
            elif dartResult[i] == '*':
                if count == 1:
                    x = int(x) * 2
                    if dartResult[i+1].isdigit():
                        count+=1
                elif count == 2:
                    x = int(x) * 2
                    y = int(y) * 2
                    if dartResult[i+1].isdigit():
                        count+=1
                else:
                    y = int(y) * 2
                    z = int(z) * 2
            elif dartResult[i] == '#':
                if count == 1:
                    x = int(x) * (-1)
                    if dartResult[i+1].isdigit():
                        count+=1
                elif count == 2:
                    y = int(y) * (-1)
                    if dartResult[i+1].isdigit():
                        count+=1
                else:
                    z = int(z) * (-1)
    
    result = x + y + z
    return result


solution('1D2S#10S')