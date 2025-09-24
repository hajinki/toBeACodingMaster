a = input()
a = list(a.upper())
b = list(set(a))
c = list(set(a))

for n in b :
    b[b.index(n)] = a.count(n)

if b.count(max(b)) == 1 :
    print(c[b.index(max(b))])
else :
    print('?')