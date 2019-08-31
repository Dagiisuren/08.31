n, m = [int(x) for x in input().split()]
niilber = 0 
for i in range(n, m + 1):
    if i % 5 == 0:
        niilber = niilber + i
        print(i)
print('xariu:', niilber)