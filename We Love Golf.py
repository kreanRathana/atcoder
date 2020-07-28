
k = int(input())
a,b = (map(int,input().split()))
new_list = []
for i in range(a,b+1):
    if i%k == 0:
        print("OK")
        break
else:
    print('NG')