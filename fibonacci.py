n = int(input())
a = 0
b = 1
if n >= 0:
    print(a)

if n >= 1:
    print(b)
ans = a + b
# count = 1

while a+ b <= n:
    ans = a + b
    print(ans)
    a = b
    b = ans
    # count += 1

