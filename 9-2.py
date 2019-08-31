a, b = [int(x) for x in input().split()]
niilber = 0
for i in range(a,b + 1):
    print(i)
    if i % 2 == 1:
        niilber = niilber + i
print('niilber:',niilber)
    
