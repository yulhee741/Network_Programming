days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30,
        'December':31 }

print("월을 입력해 주세요.")
month = input()

if month in days:
    print(month, "의 일수는: " , days[month])
else:
    print("월을 제대로 입력해 주세요.")
    month = input()
print("\n")

res = sorted(days.items())
print("알파벳 순서로 월 출력 : ", res)
print("\n")

print("일수가 31인 월을 출력 : ")
for k, v in days.items(): 
    if v == 31 : 
        print(k)
print("\n")

print("월의 일수를 기준으로 오름차순 쌍을 출력: ")
sorted_values = sorted(days.items(), key = lambda x : x[1])
print(sorted_values)
print("\n")

print("월의 3자리만 입력해주세요")
find_mon = input()
for k, v in days.items():               
    if k[0:3] == find_mon:
        print(v) 