testcase = int(input())

for i in range(0,testcase):
    x,y = map(int, input().split())
    
    if x in range(1,7) and y in range(1,7):
        if x+y > 6:
            print('YES')
        elif x+y <= 6:
            print('NO')
    else:
        print('X and Y should be less than 6')
    