a1 = int(input("enter 1st number"))
b1 = int(input("enter 2nd number"))


def gcd(a, b):
    if a == 0:
        return b;
    return gcd(b % a, a);


print(gcd(a1, b1))

