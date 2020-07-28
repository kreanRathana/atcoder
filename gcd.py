from functools import reduce
n,k = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
m1 = 1
m2=1
# for i in range(k):
#     m1 = m1 * list1[i]
#     m2 = m2 * list1[(n-1)-i]
m1 = reduce((lambda x, y: x * y), list1[k:])
m2 = reduce((lambda x, y: x * y), list1[:n-k])
# if m1 > m2 :
#     print(m1)
# else:
#     print(m2)
print(m1,m2)