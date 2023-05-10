x = str(input())
z = []
o = []
for letters in x:
    if letters == 'z':
        z.append(letters)
    else:
        o.append(letters)
if len(z)*2 == len(o):
    print('Yes')
else:
    print('No')