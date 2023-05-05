# cook your dish here
t = int(input())

for testcases in range(t):
    x, y = map(int, input().split())
    
    if y >= 2*x:
        print(x*5)
    else:
        print((y*2)+(x*1))