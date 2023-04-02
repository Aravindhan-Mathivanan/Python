# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())
    consonant_count = 0 # It is placed inside the for loop so that it would start at 0 for every new string 's'

    for i in s:
        if i in 'aeiou':
            consonant_count = 0
        else:
            consonant_count += 1
            if consonant_count >= 4:
                print('NO')
                break
            # break function stops printing 'NO' as soon as the condition is  met
            # otherwise if the code finds  more than 4 consonants in the string each time it'll print 'NO'
    else:
        print('YES')