n = int(input())
village = input()[:n]

if 'HH' in village:
    print('NO')
else:
    print('YES')
    print(village.replace('.','B'))