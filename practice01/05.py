l = [10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 40, 43, 44, 46, 50]
count = 0
sum = 0

for i in l:
    if i % 3 == 0:
        count += 1
        sum += i
print('주어진 리스트에서 3의 배수의 개수 =>', count)
print('주어진 리스트에서 3의 배수의 합 =>', sum)
