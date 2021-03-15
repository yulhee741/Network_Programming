
print("최대 공약수를 구하는 프로그램입니다. 두 수를 입력해주세요. ex)20 17")
num = tuple(map(int, input().split()))

high = max(num)
low = min(num)

while low != 0:
    re = high % low
    high = low
    low = re

print("최대 공약수 : ", high)