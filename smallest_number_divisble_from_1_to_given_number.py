from math import gcd
x = int(input('Enter a number for LCM of 1 to given number : '))
def lcm_range(n):
    lcm = 1
    for i in range(2, n+1):
        lcm = (lcm * i) // gcd(lcm, i)
    return lcm
print(lcm_range(x))

