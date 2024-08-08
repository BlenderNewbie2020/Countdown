from itertools import chain, combinations_with_replacement, permutations, zip_longest

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
