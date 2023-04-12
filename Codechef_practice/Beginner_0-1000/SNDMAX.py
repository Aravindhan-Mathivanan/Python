# cook your dish here
t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    
    
    x = n.index(max(n))
    n.pop(x)
    
    print(max(n))