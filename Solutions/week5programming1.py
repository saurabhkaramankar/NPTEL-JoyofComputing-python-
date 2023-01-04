def count_letters(S):
  d={}
  for i in S:
    d[i]=0
  for i in S:
    d[i]+=1
  return d
if __name__ == "__main__":
    S = input()
    d = count_letters(S)

d1 = {}
for i in S:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
if d1 == d:
    print(d1)
else:
    print('no')