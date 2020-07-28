
n = int(input())
t = input()
list1 = []
list2 = []
for i in range(0,(3**n)):
    list1.append(i)
for j in t:
    if j == 'S':
        for v, k in enumerate(list1):
            if k == 1:
                list1[v] = 2
            elif k == 2:
                list1[v] = 1
# lis = []
    elif j == "R":
        for o in range(0,len(list1)):
            if o == list1[-1]:
                list2.append(list1[i])
            else:
                list2.append(i)
    list1.clear
    list1.extend(list2)
print(list1)

