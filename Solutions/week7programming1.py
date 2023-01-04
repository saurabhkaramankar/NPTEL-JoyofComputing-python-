def DiagCalc(M):
    L = 0
    R = 0
    l =0
    for i in range(len(M)-1,-1,-1):
         L += M[l][l]
         R += M[l][i]
         l+=1
    print(L)
    print(R,end="")

n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

DiagCalc(M)