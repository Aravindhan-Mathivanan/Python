# cook your dish here
t = int(input())

for i in range(t):
    A,B = map(int, input().split())
    if A > B:
        print('A')
    elif B > A:
        print('B')