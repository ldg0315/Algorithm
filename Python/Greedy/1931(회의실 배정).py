import sys
n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
temp = arr[0]

for i in range(1, n):
    if arr[i][0] >= temp[1]:
        temp = arr[i]
        cnt += 1
print(cnt)