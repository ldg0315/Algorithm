n = input()
res = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)
