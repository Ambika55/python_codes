from decimal import *

import math
n = int(input())
m = int(input())

s = str(math.sqrt(n))

# arr = [None] * len(s)
ans = ""
# k = 0
r = len(s)
for j in range(0, r):
    # arr[k] = s[j]
    ans = ans + str(s[j])
    # k += 1
    if s[j] == ".":
        for i in range(1, m + 1):
            # arr[k] = s[j + i]
            ans = ans + str(s[j + i])
            # k += 1
        break

print(ans)

