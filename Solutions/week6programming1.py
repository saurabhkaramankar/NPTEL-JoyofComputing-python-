L=[int(i) for i in input().split()]
D=dict()
for i in range(len(L)):
  if L[i] not in D:
    D[L[i]]=[i]
  else:
    D[L[i]]=D[L[i]]+[i]
p=list(D.keys())[:]
for k in p:
  if len(D[k])<2:
    D.pop(k)
print(D,end="")