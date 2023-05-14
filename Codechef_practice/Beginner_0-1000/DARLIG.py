# cook your dish here
for t in range(int(input())):
    n,k = map(int, input().split())
    
    if k == 0:
        if n % 4 !=0:
            print('On')
        else:
            print('Off')
    elif k == 1:
        if n % 4 == 0:
            print('On')
        else:
            print('Ambiguous')
