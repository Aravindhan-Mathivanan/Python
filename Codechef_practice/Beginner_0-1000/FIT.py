# cook your dish here
T = int(input())

for i in range(0,T):
    x = int(input())
    if 1 <= x <= 10:
        print((x*2)*5)
    else:
        print('x out of range')