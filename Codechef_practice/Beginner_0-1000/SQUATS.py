# cook your dish here
x = int(input())
for i in range(0,x):
    squats = map(int, input().split())
    for nums in squats:
        print(nums*15)