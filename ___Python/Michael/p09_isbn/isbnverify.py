def verify(isbn):
  p = 1 # aktuell untersuhte isbn-Position
  i = 0
  sum = 0
  for c in isbn:
    i += 1
    if (c == "-"):  # - wird ignoriert
      continue
    # isbn-Position 1 - 9
    if (p < 10):
      try:
        z = int(c)
      except:
        return False
      # c ist valide Ziffer
      sum += z * (11 - p)
      p += 1
    # isbn-Position 10
    else:
      if len(isbn) > i:  # 10. isbn-Position nicht letzte Position
        return False
      if (c == "X"):
        c = 10
      try:
        z = int(c)
      except:
        return False
      # c ist valide Ziffer oder X
      sum += z
      return (sum % 11 == 0)
  return False  # Schleife hat 10. isbn-Position nicht erreicht
