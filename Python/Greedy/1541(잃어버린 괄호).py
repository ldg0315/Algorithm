# 55+50-40
n = input().split("-") # [55+50,40]

res1 = []
for i in n: # len(n) = 2
    n2 = list(map(int, i.split('+')))  #[[55,50], [40]]
    #print(sum(n2)) #sum(n2) = 105, 40
    res1.append(sum(n2)) # res1 = [105, 40]
# 첫 번째 요소 다 더함
# 첫 번째를 제외한 나머지 다 더해서 빼야함

for j in range(1, len(res1)):
    res1[0] -= res1[j]
print(res1[0])




#print(n) #[[55], [50, 40]]

#  for j in n[1:]:
#     res = j- res
# print(res)