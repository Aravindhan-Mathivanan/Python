# cook your dish here
for t in range(int(input())):
    n = int(input())
    o = map(int, input().split(' '))
    a = map(int, input().split(' '))
    o_streak = 0
    a_streak = 0
    o_max = 0
    a_max = 0
    for oi in o:
        if oi != 0:
            o_streak += 1
        else:
            o_streak = 0
        o_max = max(o_max,o_streak)
    for ai in a:
        if ai != 0:
            a_streak += 1
        else:
            a_streak = 0
        a_max = max(a_max,a_streak)
    if o_max > a_max:
        print("Om")
    elif o_max < a_max:
        print("Addy")
    else:
        print("Draw")