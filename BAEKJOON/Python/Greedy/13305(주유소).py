n = int(input())

dist = list(map(int, input().split()))
price = list(map(int, input().split()))

res = dist[0]*price[0]
temp = price[0]

for i in range(1, n-1):
    if price[i] < temp:
        temp = price[i]
    res += temp*dist[i]
print(res)
