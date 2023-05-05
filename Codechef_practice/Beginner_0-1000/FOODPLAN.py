# cook your dish here
t = int(input())

for testcases in range(t):
    n,m = map(int, input().split())
    offer = (n-((10/100)*n))
    
    if offer < m:
        print('ONLINE')
    elif offer > m:
        print('DINING')
    elif offer == m:
        print('EITHER')