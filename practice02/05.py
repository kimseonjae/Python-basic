# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
import random

def Sum(*arg):
    total = 0
    for n in arg:
        total += n
    return total

print(Sum(1, 2))
print(Sum(1, 2, 5, 7, 2, 3))