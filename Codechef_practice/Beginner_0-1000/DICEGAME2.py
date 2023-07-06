# cook your dish here
for t in range(int(input())):
    rolls = list(map(int,input().split(' ')))
    alice = list(rolls[:3])
    bob = list(rolls[3:])
    a = []
    b = []
    while len(a) < 2:
        a.append(max(alice))
        alice.pop(alice.index(max(alice)))
        b.append(max(bob))
        bob.pop(bob.index(max(bob)))
    a_score, b_score = sum(a), sum(b)
    
    if a_score > b_score:
        print("Alice")
    elif a_score < b_score:
        print("Bob")
    elif a_score == b_score:
        print('Tie')