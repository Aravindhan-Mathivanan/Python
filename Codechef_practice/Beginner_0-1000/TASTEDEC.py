# cook your dish here
t = int(input())

for testcases in range(t):
    x, y = map(int, input().split())
    bar = x*2
    candy = y*5
    if bar > candy:
        print('Chocolate')
    elif bar == candy:
        print('Either')
    else:
        print('Candy')