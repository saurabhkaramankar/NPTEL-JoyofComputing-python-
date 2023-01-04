L = list(map(int, input().split()))
zeroes = L.count(0)
i=0
while i<len(L)-zeroes:
  if L[i] == 0:
    L.pop(i)
    L.append(0)
    i-=1
  i+=1
print(L,end="")