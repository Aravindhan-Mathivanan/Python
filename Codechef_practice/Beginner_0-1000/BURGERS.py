# cook your dish here
t = int(input())

for i in range(0,t):
    
    A,B = map(int, input().split())
    if A > B:
        print(B)
    else:
        print(A)