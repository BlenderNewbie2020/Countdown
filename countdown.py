"""
Python script to attempt to solve the Channel 4 Countdown numbers game by brute force.
"""

from itertools import chain, combinations_with_replacement, permutations, zip_longest

# Define the numbers list and a target
numbers = [75, 5, 9, 3, 8, 10]
target = 699

# Generate all possible partitions of the numbers
# Generate partitions for each tuple
# Slice the tuple permutations into tuple sub-partitions
# Generate the Cartesian product of all permutations of numbers and operators
cartesian_product = (
    (x, y)
    for x in (
        " ".join((map(str, i))).replace(",", "").split(" ")
        for i in (
            [i for i in y if i]
            for y in (
                chain.from_iterable(
                    [[(i[0], i[1]), i[2]], [i[0], (i[1], i[2])]] if len(i) == 3 else i
                    for i in chain.from_iterable(
                        [
                            [i for i in j if i]
                            for j in [
                                [l[:i], l[i:j], l[j:]]
                                for i in range(1, len(l) + 1)
                                for j in range(i + 1, len(l) + 1)
                            ]
                        ]
                        for l in (
                            c
                            for i in range(2, len(numbers) + 1)
                            for c in permutations(numbers, i)
                        )
                    )
                )
            )
        )
    )
    for y in (
        p
        for r in range(2, 7)
        for p in combinations_with_replacement(["+", "-", "*", "/"], r - 1)
    )
    if len(x) == len(y) + 1
)

# Zip the Cartesian product using itertools.zip_longest
zipped_product = (
    "".join(
        tuple(item for sublist in zip_longest(*x, fillvalue="") for item in sublist)
    )
    for x in cartesian_product
)

# Evaluate each string, printing strings that equal the target
result = (i for i in zipped_product if eval(i) == target)
print(list(result))
