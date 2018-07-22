n = str(input())

multiplier = 1
ans = 0
length = len(n) - 1

for i in n:
    ans += int(i) * 2 ** length
    length -= 1

print(ans)


