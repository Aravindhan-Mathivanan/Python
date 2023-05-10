N = int(input())
data = map(str, input().split()[:N])
l = ''
for nums in data:
    l += nums[:-2:-1]
l = int(l)

if l%10 == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)