n = int(input())

num = 1
for i in range(0, n , 1):
    num = 1
    for nsp in range(n - i, 0, -1):
        print(num, end=' ')
        num += 1
    for nst in range(2 * i - 1):
        print("*", end=' ')
    print()

