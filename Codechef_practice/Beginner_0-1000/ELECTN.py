# cook your dish here
t = int(input())

for i in range(t):
    n,x = map(int, input().split())
    count = 0
    a = list(map(int, input().split()))
        
    for nums in a:
        if nums >= x:
            count += 1
    print(count)