# cook your dish here
t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    
    if 1 <= x < y <= 10:
        print(y-x)