S=input()
ans=str()
for i in S:
  if i.islower()==True:
    if i=='a':
      ans+='y'
    elif i=='b':
      ans+='z'
    else:
      ans+=chr(ord(i)-2)
  elif i.isupper()==True:
    if i=='A':
      ans+='X'
    elif i=='B':
      ans+='Y'
    elif i=='C':
      ans+='Z'
    else:
     ans+=chr(ord(i)-3)
  else:
   ans+=i
print(ans,end="")