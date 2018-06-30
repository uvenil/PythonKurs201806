import random

def muenzwurf():
  return random.randint(0,1)

def wuerfeln3():
  binaer = 1
  for i in range(3):
    binaer += 2 ** i * muenzwurf()
  if binaer > 6:
    return wuerfeln3()
  return binaer

def fair(testfkt):
  d = {}
  for i in range(10000):
    w = str(testfkt())
    if w in d:
      d[w] += 1
    else:
      d[w] = 1
  print(str(testfkt) + ": ")
  print(d)

fair(muenzwurf)
fair(wuerfeln3)
