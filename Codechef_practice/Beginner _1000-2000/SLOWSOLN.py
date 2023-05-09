# cook your dish here
t = int(input())

for testcases in range(t):
    maxT, maxN, sumN = map(int, input().split())
    max_itr = 0
    N = []
    if maxT*maxN <= sumN:
        for nums in range(maxT):
            max_itr += (maxN**2)
        print(max_itr)
    
    elif maxT*maxN > sumN:
        while True:
            if maxN < sumN:
                a = sumN-maxN
                N.append(maxN)
                sumN -= maxN

            else:
                N.append(sumN)
                break
        
        for i in N:
            max_itr += i**2
        print(max_itr)
        
        