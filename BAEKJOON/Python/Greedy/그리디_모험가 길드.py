n = int(input())
s_level = list(map(int, input().split()))
s_level.sort()

group = 0
num_people = 0

for i in s_level:
    num_people += 1 # 현재 그룹에 모험가 포함
    if num_people >= i: # 공포도가 그룹에 있는 모험가보다 작다면 그룹에 포함
        group += 1
        num_people = 0
print(group)
