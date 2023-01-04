s = input(" ").lower()

if list(s)==list(s)[::-1]:
  print("palindrome",end="")
  
else:
  print("not palindrome",end="")