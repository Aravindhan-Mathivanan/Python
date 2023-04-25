# cook your dish here
t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())
    credit = (x*4)+(y*2)
    print(credit)