b = int(input())
res = 0
for i in range(1, b + 1):
    if b % i == 0:
        print(i)
