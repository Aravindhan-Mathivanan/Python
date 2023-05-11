for r in range(int(input())):
    l = int(input())
    string = input()[:l]
    string = string.replace('.','')
    
    if string == '':
        print('Valid')
    elif string[0] == 'T':
        print('Invalid')
    elif 'HH' in string:
        print('Invalid')
    elif 'TT' in string:
        print('Invalid')
    elif len(string)%2 != 0:
        print('Invalid')
    else:
        print('Valid')
