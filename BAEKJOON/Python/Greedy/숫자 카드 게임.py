n, m = map(int, input().split())
res = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    low_num = min(arr)
    res = max(res, low_num)

print(res)