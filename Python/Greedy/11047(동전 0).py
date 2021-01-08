n, k = map(int, input().split())

money = []
cnt = 0

for _ in range(n):
  money.append(int(input()))

money.sort(reverse = True)

for i in money:
  if k >= i:
    cnt += k // i
    k %= i
  else:
    pass
print(cnt)