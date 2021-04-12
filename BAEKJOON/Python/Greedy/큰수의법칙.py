n, m, k = map(int, input().split())
item = list(map(int, input().split()))

item.sort()
fir = item[-1]
sec = item[-2]
res = 0

while True:
  for i in range(k):
    if m == 0:
      break
    else:
      res += fir
      m -= 1
  if m == 0:
    break
  else:
    res += sec
    m -= 1
print(res)