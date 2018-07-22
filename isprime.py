num = int(input())

count = 0
i = 2

while i < num:
    if num % i == 0:
        count += 1
    i += 1

if count == 0:
    print("prime")
else:
    print("Not prime")

