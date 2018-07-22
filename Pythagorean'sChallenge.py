import math

t = int(input())
for x in range(0, t):
    n = int(input())
    a= math.sqrt(n)
    for i in range(0, int(a)+1):
        for j in range(i, int(a)+1):
            sum = i ** 2 + j ** 2
            if sum == n:
                print("(" + str(i) + "," + str(j) + ")")
    print()


