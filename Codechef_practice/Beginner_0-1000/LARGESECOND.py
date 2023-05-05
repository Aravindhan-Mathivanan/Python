# cook your dish here
t = int(input())

for testcases in range(t):
    n = int(input())
    b = []
    
    a = map(int, input().split()[:n])
    
    super_set = list(set(a))
    
    if len(super_set) > 0:
        x = max(super_set)
        super_set.remove(x)
    if len(super_set) > 0:
        y = max(super_set)
        super_set.remove(y)
    
    print(x+y)