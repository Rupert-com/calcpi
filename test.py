from time import time_ns
def zufall(seed,m=2**32,a=101427,b=321):
    x_a = seed
    for i in range(m):
        x_a =(a*x_a+b)%m
    return x_a    
for i in range(10):
  print (zufall(seed=time_ns(), m=2**16))