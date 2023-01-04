def isPrime(num):
    if num == 2:
        return True
    
    if num<2:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
        
    return True


a = int(input())
b = int(input())

for i in range(a, b+1):
    if not isPrime(i):
        print(i)


#approach2

def check_prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
      f=1
      break
  return(f==0)


a=int(input())
b=int(input())
for i in range(a,b+1):
   if check_prime(i)==False:
     print(i)