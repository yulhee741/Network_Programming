def sum(num):
    str_n = str(num)
    sum_n = 0

    for _ in str_n:
        sum_n += int(_)
    return sum_n

total = 0
for i in range(1, 1001):
    total = total + sum(i)
print(total)