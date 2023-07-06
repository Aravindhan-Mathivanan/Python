n = int(input())
m = list(map(int, input().split()[:n]))
singers = {}
fav_singers = 0
for i in m:
    if i in singers:
        singers[i] += 1
    else:
        singers[i] = 1

max_singer = max(singers.values())

for values in singers.values():
    if values == max_singer:
        fav_singers += 1

print(fav_singers)