m,c = map(int,input().split())
a = ['+' for i in range(c+1)]
d = ['|' for i in range(c+1)]
e = '-'.join(a)
f = '.'.join(d)
for j in range(m):
 print(e)
 print(f)
print(e,end = '')