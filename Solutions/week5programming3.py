L = [int(i) for i in input().split()]
import math
def isprime(n):
  if n>1:
    for i in range(2,n):
      if n%i==0:
        return False
    return True

for k in L:
  if isprime(k):
    print(k,end="")
    break
  else:
    continue