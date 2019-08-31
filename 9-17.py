k = int(input())
for i in range(101,1000):
    if i // 100 + i % 100 //10 + i % 10 == k:
        print(i)