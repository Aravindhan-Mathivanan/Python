# cook your dish here
t = int(input())

for i in range(t):
    a,b,c = map(int, input().split())
    
    if a+b+c <= 101:
        if a > 50:
            print('A')
        elif b > 50:
            print('B')
        elif c > 50:
            print('C')
        
        else:
            print('NOTA')