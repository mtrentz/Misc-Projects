from itertools import permutations
from itertools import combinations

"""
My take on the following challenge:

Write a program that outputs all possibilities to put + or - or nothing between the numbers 1,2....9
(in this order) such that the result is 100. For example: 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100
"""


def revr(num):
    """Either changes sign of number of whole list"""
    if isinstance(num, int):
        return -num
    else:
        for i in range(len(num)):
            num[i] = revr(num[i])
        return num


def sum_lista(lista):
    """Summs list and check if it matches with desired result"""
    if sum(lista) == result:
        combinacoes.append(lista.copy())
        return sum(lista)
    else:
        return sum(lista)


def testa_sinais(lista):
    """Checks sum of all possible combinations of sign in list members"""
    orig = lista.copy()
    for index1 in range(1,len(lista)+1):
        if len(lista) == 1:
            sum_lista(lista)
            break
        combs = combinations(range(0, len(lista)), index1)
        for c in combs:
            for index2 in c:
                lista[index2] = revr(lista[index2])
            sum_lista(lista)
            lista = orig.copy()


def listnum_to_listchar(lista):
    """Changes list of ints to list of chars"""
    strlist = []
    for c in lista:
        strlist.append(str(c))
    return strlist


def listchar_to_listnum(lista):
    """Changes list of chars to list of ints"""
    numlist = []
    txt = ""
    for n in lista:
        txt += n
    txt = txt.split()
    for c in txt:
        numlist.append(int(c))
    return numlist


combinacoes = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_strlist = listnum_to_listchar(nums)
result = 100

# If I want a sum of (1 +/- 2 +/- 3 ... +/- 9) I would find it here.
testa_sinais(nums)

# Starting with single item as [123456789] and then adding spaces in between numbers.
for k in range(1, len(nums)):
    # Calculates every combination of adding 1 space, then 2, then 3, etc...
    perms = combinations(range(1, len(nums)), k)
    for p in perms:
        spaces = sorted(p)
        orig = nums_strlist.copy()
        if len(spaces) < 0:
            pass
        else:
            for i in range(len(nums)-1, 0, -1):     # Goes backwards to not have indexation problems
                if i in spaces:
                    nums_strlist.insert(i, " ")
                    test_numslist = listchar_to_listnum(nums_strlist)
                    testa_sinais(test_numslist)
        nums_strlist = orig.copy()


print("-"*30)
final_list = []    # Filtering duplicated results
for r in combinacoes:
    if r not in final_list:
        final_list.append(r)
        print(r)


# Checking results
print('')
print('SUMS:')
for lis in final_list:
    print(sum(lis))
