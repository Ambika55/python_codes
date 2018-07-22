print("input sides of triangle")

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x == y == z:
    print("equilateral triangle")
else:
    if x != y != z:
        print("scalene triangle")
    else:
        print("isosceles triangle")

