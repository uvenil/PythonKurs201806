from random import Random

class Wuerfel(object):
  def __init__(self):
    self.r = Random()

  def __iter__(self):
    return self

  def __next__(self):
    return self.r.randint(1, 6)

w = Wuerfel()
for a in w:
  print(a)