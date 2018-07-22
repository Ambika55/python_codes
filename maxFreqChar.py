s = str(input())

max = 0
ch = ''
for i in range(0, len(s)):
    count = 1
    for x in range(i + 1, len(s)):
        if s[i] == s[x]:
            count += 1
    if count > max:
        max = count
        ch = s[i]

print(ch)

