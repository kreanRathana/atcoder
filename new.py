get = int(input())
j = 0
for i in range(get + 1):
    if i % 3 != 0 and i % 5 != 0:
        j = j + i
print(j)
# print(sum([i for i in range(1, a+1) if (i%3) != 0 and (i%5) != 0]))