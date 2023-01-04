items=[x for x in input().split('#')]
items.sort(reverse = True)
print ('#'.join(items))

#solution2
L=input().split("#")
print("#".join(sorted(L,reverse=True)),end="")