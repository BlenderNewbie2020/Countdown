"""
Python script to attempt to solve the Channel 4 Countdown numbers game - Dictionary method

Create a dictionary of plus/minus combinations then combine with
times/divide if length = 6 and numbers are unique
"""

from itertools import chain, combinations, product
from more_itertools import roundrobin

numbers = ['75', '5', '9', '3', '8', '10']
ops_md = ['*', '/']
ops_pm = ['+', '-']
target = 699

'''
use the walrus operator to create the partition key and result value on the fly
only if the value is an integer and positive. Use more_itertools.roundrobin for
efficiency
'''
infix_pm = {(len(x), xy):int(z)
              for x in (c for i in range(2, len(numbers)+1) for c in combinations(numbers, i))
              for y in (p for p in product(ops_pm, repeat=len(x)-1))
              if len(x)==len(y)+1
              if (z:=eval(xy:=''.join(roundrobin(x, y))))%1==0
              if z>0
              }

print(infix_pm)
