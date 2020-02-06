 
from itertools import permutations

"""
My take on the challenge from:
https://rosettacode.org/wiki/4-rings_or_4-squares_puzzle
"""

def test_equal(list):
    if sq1 == sq2 == sq3 == sq4:
        possibs.append(list)

possibs = []

vals = [i for i in range(1,8)]

# All permutations of these values
perms = permutations(vals)

for p in perms:
    sq1 = sum(p[0:2])
    sq2 = sum(p[1:4])
    sq3 = sum(p[3:6])
    sq4 = sum(p[5:8])
    test_equal(p)


for c in possibs:
    print(c)
