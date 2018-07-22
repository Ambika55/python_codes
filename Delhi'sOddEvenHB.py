t = int(input())

for x in range(0, t):
    oddsum = 0
    evensum = 0
    n = input()
    for i in n:
        if int(i) % 2 == 0:
            evensum += int(i)
        else:
            oddsum += int(i)

    if oddsum % 3 == 0 :
        print("YES")
    else:
        if evensum % 4 == 0 :
            print("YES")
        else:
            print("NO")

