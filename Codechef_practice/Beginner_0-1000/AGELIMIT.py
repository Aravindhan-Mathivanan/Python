# cook your dish here
def age_limit():
    testcases = int(input())
    
    for i in range(0,testcases):
        X,Y,A = map(int, input().split())
        if 20<= X < Y <= 40 and 10 <= A <= 50:
            if A in range(X,Y):
                print('YES')
            else:
                print('NO')
        else:
            print('Input out of range')

age_limit()