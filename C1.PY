n = int(input())
list1 = list(map(int,input().split()))
su =0
for i in range(1,n+1,2):
    if list1[i-1] % 2 != 0:
        su =su +1
print(su)