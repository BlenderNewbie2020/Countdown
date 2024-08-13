from itertools import chain, combinations_with_replacement, permutations, zip_longest

'''
# comment out the original code and keep for reference

# Define the two lists
numbers = [75, 5, 9, 3, 8, 10]
operators = ['+', '-', '*', '/']
target = 699

def daisy(l):
    k = ([[i for i in j if i]
          for j in [[l[:i], l[i:j], l[j:]]
                    for i in range(1,len(l)+1)
                    for j in range(i+1,len(l)+1)]])
    if len(k) > 3:
        return chain.from_iterable([[(i[0], i[1]), i[2]], [i[0], (i[1], i[2])]]
                                   for i in k if len(i)==3)
    return k
'''

'''
# Use the python console to make a dictionary
>>> numbers = [75, 5, 9, 3, 8, 10]

# make the numbers strings because converting Python types is a pain
>>> numbers = ['75', '5', '9']
>>> operators = ['+', '-', '*', '/']
>>> target = 699

# make lists of the permutations and operators for testing
>>> combis = [c for i in range(2, len(numbers)+1) for c in permutations(numbers, i)]
>>> symbol = [p for r in range(2,7) for p in combinations_with_replacement(operators, r-1)]

# verify the permutations tuples
>>> test_digits = {c:c for c in combis}
>>> test_digits
    {('75', '5'): ('75', '5'), ('75', '9'): ('75', '9'), ('5', '75'): ('5', '75'), ('5', '9'): ('5', '9'),... }

# try making a dictionary of numbers and operators
>>> test_tups = {x:(x, y) for x in combis for y in symbol if len(x)==len(y)+1}
>>> test_tups
    {('75', '5'): (('75', '5'), ('/',)), ('75', '9'): (('75', '9'), ('/',)), ... }

# zip the numbers and operators to infix notation
>>> test_zipl = {x:zip_longest(x, y, fillvalue='') for x in combis for y in symbol if len(x)==len(y)+1}
>>> test_zipl
    {('75', '5'): [('75', '/'), ('5', '')], ('75', '9'): [('75', '/'), ('9', '')], ...

# try to evaluate a chain
>>> q=(('75', '/'), ('5', ''))
>>> eval(''.join(chain(*q)))
    15.0

# make the key more meaningful
>>> test_eval = {x+y:eval(''.join(chain(*(zip_longest(x, y, fillvalue=''))))) for x in combis for y in symbol if len(x)==len(y)+1}
>>> test_eval
    {('75', '5', '+'): 80, ('75', '5', '-'): 70, ('75', '5', '*'): 375, ...}

# use the walrus operator to create the key and value on the fly
# only if the value is an integer and positive
>>> test_dict = {xy:z
        for x in combis
        for y in symbol
        if len(x)==len(y)+1
        if (z:=eval(xy:''.join(chain(*(zip_longest(x, y, fillvalue=''))))))%1==0
        if z>0}
>>> test_dict # look for no decimals or negative numbers
    {'75+5': 80, '75-5': 70, '75*5': 375, '75/5': 15.0, '75+9': 84, ...}

'''

'''
# Comment out the original code to keep for reference

# Generate all possible partitions of the numbers
step1 = [c for i in range(2, len(numbers)+1) for c in permutations(numbers, i)]

# Generate partitions for each tuple
step2 = (chain.from_iterable([daisy(l) for l in step1]))

# Generate the Cartesian product of all permutations of numbers and operators
cartesian_product = ((x, y)
    for x in (' '.join((map(str, i))).replace(',', '').split(' ') 
              for i in ([i for i in y if i] for y in step2))
    for y in [list(p)
              for r in range(2, 7)
              for p in combinations_with_replacement(operators, r - 1)]
    if len(x) == len(y) + 1)

# Zip the Cartesian product using itertools.zip_longest
zipped_product = (''.join(
    tuple(item
          for sublist in zip_longest(*x, fillvalue='')
          for item in sublist))
                  for x in cartesian_product)

result = (i for i in zipped_product if eval(i) == target)

print(list(result))
