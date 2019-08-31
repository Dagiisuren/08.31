a, b = [int(x) for x in input().split()]
niilber = 0
for i in range(a, b + 1):
    if i % 2 == 0: 
        niilber = niilber + i
        print(i)
print('niilber:',niilber)
