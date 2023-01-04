s= input()
l =list('aeiou')
a=""
for i in s:
  if i.lower() in l:
    a=a+'*'
  else:
    a=a+i
print(a,end="")