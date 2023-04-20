# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    x = n
    chrg = 0

    while True:
        if x < 50:
            x += 2
            chrg += 1
        elif x > 50:
            x -= 3
            chrg += 1
        elif x == 50:
            break
        
    print(chrg)