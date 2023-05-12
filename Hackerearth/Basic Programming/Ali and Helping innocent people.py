tag = input()[:9]
num = []
truck = 'valid'

for digits in tag:
    if digits in ['A', 'E', 'I', 'O', 'U', 'Y']:
        truck = 'invalid'
        break
    elif digits in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        digits = int(digits)
        num.append(digits)

for i in range(len(num)-1):
    if i != 1 and i != 4:
        if (num[i] + num[i+1]) % 2 == 0:
            if truck != 'invalid':
                truck = 'valid'

        elif (num[i] + num[i+1]) % 2 != 0:
            truck = 'invalid'

print(truck)