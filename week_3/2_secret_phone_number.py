def solution(phone_number):
    secret_num = len(phone_number[:-4])
    result = '*' * secret_num
    result += phone_number[-4:]
    return result
