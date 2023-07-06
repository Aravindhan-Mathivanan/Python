# cook your dish here
for t in range(int(input())):
    bell_status = list(map(int, input().split(' ')))
    
    n, x, k, p = bell_status
    
    for bells_rang in range(1,k+1):
        if (bells_rang <= x):
            p += 10
            
        elif (x < bells_rang <= n):
            p += 5
            if (n == bells_rang):
                p += 20
            
    print(p)