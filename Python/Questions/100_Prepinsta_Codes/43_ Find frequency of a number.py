# Find frequency of a number

from collections import Counter
from itertools import repeat, chain
ini_list = [10, 20, 30, 40, 40, 50, 50, 50]

result = sorted(ini_list, key = ini_list.count, reverse = True)
print(str(result))