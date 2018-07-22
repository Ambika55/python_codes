n = int(input())

nsp = n - 1
nst = 1

for i in range(1, n + 1, 1):
    for nsp in range(n-i, 0, -1):
        print(' ', end=' ')
    for nst in range(2 * i - 1):
        print("*", end=' ')
    print()


# reverse triangle
print()

for i in range(n, 0, -1):
    for nsp in range(n-i, 0, -1):
        print(' ', end=' ')
    for nst in range(2 * i - 1):
        print("*", end=' ')
    print()
