num = int(input())
count = 0

temp = num
while temp != 0:
    temp //= 10
    count += 1

sum1 = 0
temp = num
while temp != 0:
    rem = temp % 10
    sum1 += rem ** count
    temp //= 10

if sum1 == num:
    print("armstrong number")

else:
    print("not armstrong number")
