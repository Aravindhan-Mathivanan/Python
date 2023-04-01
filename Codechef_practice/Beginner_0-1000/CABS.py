# cook your dish here
test_cases = int(input())
for test_cases in range(0, test_cases):
    cab1, cab2 = input().split()
    cab1 = int(cab1)
    cab2 = int(cab2)
    if cab1 < cab2:
        print("FIRST")
    elif cab1 > cab2:
        print('SECOND')
    elif cab1 == cab2:
        print('ANY')