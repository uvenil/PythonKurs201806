# M.h.v. Zufallszahlen
import random
import math

treffer = 0
i = 0

for i in range(1000000):
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    # (a, b) = random.uniform(0,1)
    hypotenuse = math.sqrt((a**2) + (b**2))
    if hypotenuse < 1:
        treffer += 1

print("Pi = ")
print(4*treffer/(i+1))