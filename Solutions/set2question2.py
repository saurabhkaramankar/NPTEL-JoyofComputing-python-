def convertL(L):
    d = dict()
    for i in sorted(L):
        d[i[0]] = i[1]
    sorted_values = sorted([int(i) for i in d.values()])
    sorted_dict = dict()

    for i in sorted_values:
        for k in d.keys():
            if d[k] == "+"+str(i):
                sorted_dict[k] = d[k]
    return(sorted_dict)
n = int(input())
L = []
for i in range(n):
    L.append(input().split())

print(convertL(L))