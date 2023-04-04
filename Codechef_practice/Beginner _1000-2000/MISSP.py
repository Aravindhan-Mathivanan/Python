# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    lists = []
    for j in range(n):
        types = int(input())
        lists.append(types)
    
    counts = {}
    
    for k in lists:
        if k in counts:
            counts[k] += 1
        else:
    
            counts[k] = 1
            
    for k, l in counts.items():
        if l % 2 != 0:
            print(k)
            break