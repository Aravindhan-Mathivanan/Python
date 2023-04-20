# cook your dish here
t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    
    if n > (m*6*6):
        print('NO')
    else:
        print('YES')