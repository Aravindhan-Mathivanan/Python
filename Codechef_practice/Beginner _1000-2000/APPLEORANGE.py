# cook your dish here
for t in range(int(input())):
    n, m = map(int, input().split())
    
    while(m):
        n,m = m,n%m
    print(n)