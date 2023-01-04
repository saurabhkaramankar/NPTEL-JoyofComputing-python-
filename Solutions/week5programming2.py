def uniqueE(L):
  d={}
  for i in L:
    d[i]=0;
  for i in L:
    d[i]=d[i]+1
    
  sol = []
  for key,value in d.items():
      if value==1:
          sol.append(key)
          
  sol.sort()
  return sol;
L = [int(i) for i in input().split()]
print(uniqueE(L))