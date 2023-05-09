# cook your dish here
t = int(input())

for testcases in range(t):
    n, b = map(int, input().split())
    size = []

    for varieties in range(n):
        w, h, p = map(int, input().split())
        if p <=b:
            size.append(w*h)
    
    if len(size) == 0:
        print('no tablet')
    else:
        print(max(size))


            