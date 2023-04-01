# cook your dish here
T = int(input())
for i in range(0,T):
    x,y = map(int, input().split())
    if 1 <= x <= 100 and 1 <= y <= 100:
        print(x*y)
    else:
        print('x and y out of range')