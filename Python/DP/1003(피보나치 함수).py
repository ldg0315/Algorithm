t = int(input())

for _ in range(t):
  n = int(input())
  zero = [1, 0]
  one = [0, 1]
  if n == 0:
    print("{0} {1}".format(zero[n], one[n]))
  elif n == 1:
    print("{0} {1}".format(zero[n], one[n]))
  else:
    for i in range(2, n+1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])
    print("{0} {1}".format(zero[n], one[n]))

