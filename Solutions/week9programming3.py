n = int(input())
n = str(n)
dic = {}
for i in range(len(n)):
    if n[i] not in dic.keys():
        dic[n[i]] = [i]
    else:
         dic[n[i]].append(i)
        
for key,value in dic.items():
    print(key, end= ' ')
    for i in value:
      print(i, end= ' ')
      
      
    print()