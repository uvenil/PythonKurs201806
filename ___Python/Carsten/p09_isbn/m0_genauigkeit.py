import fractions

import math

potenz = 2**4096
print(potenz)

a = fractions.Fraction(3, 4)
b = fractions.Fraction(1, 8)

c = a + b

c = c ** 4

print (c)
print(float(c))

c = math.sin(c)

print(c)
