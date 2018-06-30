from random import Random

l = [2, 3, 5, 7, 11]
for x in l:
    print(x)

s = "Hallo!"
for c in s:
    print(c)

class Wuerfel(object):
    def __init__(self):
        self.r = Random()

    def __iter__(self):
        return self

    def __next__(self):
        return self.r.randint(1, 6)

#w = Wuerfel()
#for a in w:
#    print(a)


# Generator für Fibonacci-Zahlen
# 1 1
#     2
#      3
#       5
#        8
#         13

def fib():
    a = 1
    b = 1
    while (True):
        (a, b) = (b, a + b)
        yield a

f = fib()
l = []
for i in range(10):
    l.append(next(f))
print(l)

