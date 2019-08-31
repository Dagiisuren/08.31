n , m = [int(x) for x in input().split()]
res= 0
for i in range(n, m + 1):
    if i % 2 == 1 :
        print(i)
        res += 1
print('too',res)