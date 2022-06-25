from math import asin, cos, sqrt, pi, radians, pow

x = float(input())
y = float(input())


z1 = x + sqrt(3)/2 * pi
z2 = cos(z1)
z3 = asin(z2)
z4 = 1.2*sqrt(2 - pow(cos(y),2))
z5 = z3 + z4
z6 = x**2 + y**2 +1
z = z5/z6

print(round(z,5))