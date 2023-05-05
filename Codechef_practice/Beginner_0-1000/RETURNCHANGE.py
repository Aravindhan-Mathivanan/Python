# cook your dish here
t = int(input())

for testcases in range(t):
    x = int(input())
    near = x%10
    
    if near == 0:
        print(100-x)
    elif near >= 5:
        round_up = 10-near+x
        print(100-round_up)
    elif near < 5:
        round_up = x-near
        print(100-round_up)