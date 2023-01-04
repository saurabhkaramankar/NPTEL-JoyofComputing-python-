def snake(M):
  
    ans = []
  
    for i in range(len(M)):
        if i%2 ==0:
          ans+=M[i]
        else:
          ans+=M[i][::-1]
          
            
    return (ans)
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))