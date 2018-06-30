from random import Random

class Wuerfel(object):
    def __init__(self):
        self.r = Random()

    def __iter__(self):
        return self

    def __next__(self):
        return self.r.randint(1, 6)

# w = Wuerfel()
# for a in w:
#     print(a)

# Generator für Fibonacci-Zahlen:
# a b
# 1 1
#   a b
#     2
#     a b
#       3
#         5
#           8
#             13

def fib():
    a = 1
    b = 1
    while True:
        (a, b) = (b, a + b)
        yield a

f = fib()
#for i in f:
#    print(i)
#    print()

l = [next(f) for i in range(10)]
print(l)