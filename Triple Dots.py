
k = int(input())
s = input()
n = len(s)
if  n <= k:
    print(s)
elif  n != k:
    print(s[:k]+'...')
