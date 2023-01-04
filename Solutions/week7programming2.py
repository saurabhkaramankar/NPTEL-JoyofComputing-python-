def Transpose(M):
    rowlen = len(M)
    collen = len(M[0])
    ans  = [[] for i in range(collen)]
    for i in range(collen):
        for j in range(rowlen):
            ans[i].append(M[j][i])
    return ans
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))

#solution2
def Transpose(M):
    rowlen = len(M)
    collen = len(M[0])
    ans = [[] for i in range(collen)]
    
    for i in range(collen):
        for j in range(rowlen):
            ans[i].append(M[j][i])
    return ans
    

n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))