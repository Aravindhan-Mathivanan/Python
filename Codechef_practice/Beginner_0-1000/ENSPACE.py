# cook your dish here
t = int(input())

for i in range(t):
    n, x, y = map(int, input().split())
    
    rom = x+(y*2)
    
    if n >= rom:
        print('YES')
    else:
        print('NO')