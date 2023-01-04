L = list(map(int, input().split()))


k=[0]*(max(L)+1)
for i in range(len(k)):
  if i in L:
    k[i]=i
print(*k,end="")