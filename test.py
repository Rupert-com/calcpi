def seedLCG(initVal):
  global rand
  rand = initVal

def lcg():
  a = 1664525
  b = 1013904223
  m = 2**32
  global rand
  rand = (a*rand + b) % m
  return rand

seedLCG(1)

for i in range(10):
  print (lcg())