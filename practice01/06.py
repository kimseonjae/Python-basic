# 문제6.키보드에서 정수로 된 돈의 액수를 입력 받아 오만원권, 만원권, 오천원권, 천원권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
a = int(input('금액 : '))
n = 0
while(True):
    if (a >= 50000):
        n = a / 50000
        a %= 50000
        print('50000원: %d개' %n)
    elif(50000 > a and a >= 10000):
        n = a / 10000
        a %= 10000
        print('10000원: %d개' %n)
    elif(10000 > a and a >= 5000):
        n = a / 5000
        a %= 5000
        print('5000원: %d개' %n)
    elif(5000 > a and a >= 1000):
        n = a / 1000
        a %= 1000
        print('1000원: %d개' %n)
    elif(1000 > a and a >= 500):
        n = a / 500
        a %= 500
        print('500원: %d개' %n)
    elif(500 > a and a >= 100):
        n = a / 100
        a %= 100
        print('100원: %d개' %n)
    elif(100 > a and a >= 50):
        n = a / 50
        a %= 50
        print('50원: %d개' %n)
    elif(50 > a and a >= 10):
        n = a / 10
        a %= 10
        print('10원: %d개' %n)
    elif(10 > a and a >= 5):
        n = a / 5
        a %= 5
        print('5원: %d개' %n)
    else:
        print('1원: %d개' %a)
        break

