# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

i = 0
while (i < 100):
    i += 1
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print(i, '짝')
    elif i / 10 == 3 or i / 10 == 6 or i / 10 == 9:
        print(i, "짝")