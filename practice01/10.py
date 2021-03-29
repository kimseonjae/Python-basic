# 문제 10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
#     a = 입력 받은 숫자가 홀수인 경우에는 0부터 입력 값까지 홀수의 합을 출력합니다.
#         -> 예제 : 입력이 7이면 16을 출력(1 + 3+ 5 + 7 = 16)
#     b = 입력 받은 숫자가 짝수인 경우에는 0부터 입력 값까지 짝수의 합을 출력합니다.
#         -> 예제 : 입력이 10이면 30을 출력(2 + 4 + 6 + 8 + 10 = 30)

def Even(a):
    sum = 0
    for i in range(0, a+1):
        if (i % 2 == 0):
            sum += i
    return sum

def Odd(a):
    sum = 0
    for i in range(0, a+1):
        if (i % 2 == 1):
            sum += i
    return sum

n = int(input('숫자를 입력하세요: '))
if n % 2 == 0:
    print('결과 값 : ', Even(n))
else:
    print('결과 값 : ', Odd(n))