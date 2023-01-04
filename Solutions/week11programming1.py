a=int(input())
b=int(input())
c=int(input())
L=[a,b,c]
hs=max(a,b,c)*max(a,b,c)
L.remove(max(a,b,c))
os=L[0]*L[0]+L[1]*L[1]
if os==hs:
  print("YES",end="")
else:
  print("NO",end="")