N = int(input())
K = int(input())
L = []
if K%2!=0:
  for x in range(N):
    if x%2==0:
      L.append(0)
    else:
      L.append(1)
else:
  for x in range(N):
    if x%2!=0:
      L.append(0)
    else:
      L.append(1)
print(L, end="")