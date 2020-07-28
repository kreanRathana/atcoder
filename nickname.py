a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
re1 = (t*v) + a
re2 = (t*w) + b
if re1 - re2 >=0  :
    print("YES")
else:
    print("NO")