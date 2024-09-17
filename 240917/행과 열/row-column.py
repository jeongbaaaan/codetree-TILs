#, b = map(int, input(). split())
#for i in range(1, 5):
    #for j in range(1, 6):
        #print(i * j, end=" ")
    #print()

a, b = map(int, input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i*j, end=" ")
    print()