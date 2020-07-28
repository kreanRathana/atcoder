l,r,d =map(int,input().split())
su =0
for i in range(l,r+1):
    if i % d == 0:
        su = su + 1
print(su)