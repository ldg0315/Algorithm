n = int(input())
t = list(map(int,input().split()))

t.sort()
res = 0

for i in range(n):
  for j in range(i+1):
    res += t[j]
print(res)

