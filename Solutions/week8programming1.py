def cubeT(l):
  res = tuple([pow(i,3) for i in l])
  return res
L = [int(i) for i in input().split()]
print(cubeT(L))