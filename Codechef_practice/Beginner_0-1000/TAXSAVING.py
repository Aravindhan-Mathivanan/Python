# cook your dish here
T = int(input())
for i in range(0,T):
    x,y = map(int, input().split())
    if 1 <= y < x <= 100:
        print(x-y)

    