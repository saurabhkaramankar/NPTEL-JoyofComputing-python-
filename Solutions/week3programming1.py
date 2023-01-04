L = [int(i) for i in input().split()]
result = [x for x in L if x%5==0 or x%7==0]

print(sorted(result),end="");