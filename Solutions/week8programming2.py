def isvowel(ch):
  v = 'AEIOUaeiou'
  if ch in v:
     return True
  else:
     return False
    
def replaceV(s):
   n = len(s)
   ans = ''
   i=0
   while(i<n-2):
        if isvowel(s[i]) and isvowel(s[i+1]) and isvowel(s[i+2]):
          ans = ans+'_'
          i=i+3
        else:
          ans=ans+s[i]
          i=i+1
   return ans+s[i:]
S = input()
print(replaceV(S))