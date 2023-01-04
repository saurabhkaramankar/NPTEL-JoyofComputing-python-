def mergeDic(d1, d2):
    dic = {}
    
    for key,value in d1.items():
        dic[key] = value
        
    for key,value in d2.items():
        if key not in dic.keys():
          dic[key] = value
          
    return dic
key = list(map(int, input().split()))
val = list(map(int, input().split()))

d1 = {}
for i in range(len(key)):
    d1[key[i]] = val[i]
    
d2 = {}
key = list(map(int, input().split()))
val = list(map(int, input().split()))
for i in range(len(key)):
    d2[key[i]] = val[i]

print(mergeDic(d1, d2))