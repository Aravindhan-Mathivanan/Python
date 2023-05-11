# cook your dish here
for t in range(int(input())):
    s = input().split('/')
    
    if (int(s[0]) in range(13,32)) and (int(s[1]) in range(1,13)):
        print('DD/MM/YYYY')
    elif (int(s[1]) in range(13,32)) and (int(s[0]) in range(1,13)):
        print('MM/DD/YYYY')
    else:
        print('BOTH')
