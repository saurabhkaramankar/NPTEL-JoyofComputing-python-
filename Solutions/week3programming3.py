L = [int(i) for i in input().split()]
c = 0
for i in L: 
    if i % 2 == 1:
      c+=1
print(c,end="")