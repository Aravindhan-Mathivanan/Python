for t in range(int(input())):
    g, p = map(int, input().split())
    n = int(input())
    g_bal = 0
    p_bal = 0

    for participants in range(n):
        j1, j2 = map(int, input().split())

        if t%2 == 0 :
            if (j1 == 1) and (j2 == 0):
                g_bal += 1
            elif (j1 == 0) and (j2 == 1):
                p_bal += 1
            elif (j1 == 1) and (j2 == 1):
                p_bal += 1
                g_bal += 1
        elif t%2 != 0:
            if (j1 == 1) and (j2 == 0):
                p_bal += 1
            elif (j1 == 0) and (j2 == 1):
                g_bal += 1
            elif (j1 == 1) and (j2 == 1):
                p_bal += 1
                g_bal += 1
    print((g*g_bal)+(p*p_bal))