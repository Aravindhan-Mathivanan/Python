# cook your dish here
t = int(input())

for testcases in range(t):
    a, b, c = map(int, input().split())
    if (a>b) and (a>c):
        print('Alice')
    elif (b>c) and (b>a):
        print('Bob')
    elif (c>a) and (c>b):
        print('Charlie')