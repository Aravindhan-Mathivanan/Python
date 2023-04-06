# cook your dish here
t = int(input())

for i in range(t):
    n,K = map(int, input().split())
    a = list(map(int, input().split()))
    protein = 0
    day = -1

    for j in range(n):
        protein += a[j]
        if protein < K:
            day = j + 1
            break
        protein -= K

    if day == -1:
        print('YES')
    else:
        print(f'NO {day}')