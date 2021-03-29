# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
while(True):
    v = 0
    a = input('숫자를 입력해주세요. ')
    for i in a:
        if (48 <= ord(i) and ord(i) <= 57):
            v += ord(i)
        else:
            v = str(v)
    if (type(v) == int):
        if v % 3 == 0:
            print('3의 배수 입니다')
        elif v % 3 != 0:
            print('3의 배수가 아닙니다.')
    else:
        print('정수가 아닙니다.')