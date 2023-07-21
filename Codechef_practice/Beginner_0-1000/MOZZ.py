# cook your dish here
for t in range(int(input())):
    x, y, r = list(map(int, input().split(' ')))
    sticks = r//30
    total = x + sticks
    plates = 0
    while total > y:
        plates += 1
        total -= y
    if total > 0:
        print(plates + 1)
    else:
        print(plates)