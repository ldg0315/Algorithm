n = int(input())
res = list(map(int, input().split()))

dp = [0] * 100
dp[0], dp[1] = res[0], max(res[0], res[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + res[i]) 
print(dp[n-1])