# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    for x in a:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    
    valid = True
    for x in freq:
        if freq[x] > 2:
            valid = False
            break
    
    if valid:
        print("Yes")
    else:
        print("No")