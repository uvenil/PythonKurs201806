import fractions
import math

potenz = 2 ** 4096
print(potenz)

a = fractions.Fraction(3, 4)
b = fractions.Fraction(1, 8)

c = a + b + 1
print(c)

c = c ** 1024
print(c)
print(float(c))

c = math.sin(c)
print(c)
