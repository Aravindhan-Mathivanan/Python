# cook your dish here
t = int(input())

for i in range(t):
    A = list(map(int,input().split()))
    if A[2] in A[0:2] and A[3] in A[0:2]:
        print(1, end = '')
    elif A[4] in A[0:2] and A[5] in A[0:2]:
        print(2, end = '')
    else:
        print(0)
    
    print()