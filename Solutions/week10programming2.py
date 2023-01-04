def closestSchool(X, Y, L):
  d=[((X-i[0])**2+(Y-i[1])**2)**0.5 for i in L]
  for i in range(len(d)):
    if d[i]==min(d):
      print(L[i])
x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)