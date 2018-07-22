n = int(input())

for i in range(1, n + 1):
    s = ""
    num = 1
    for j in range(1, i + 1):
        # print(num, end='')
        s = s+str(num)
        num += 1
    for k in range(1, n - i + 1):
        # print("*", end='')
        s += "*"
    # for p in s:
    #     print(p, end="")
    print(s)



