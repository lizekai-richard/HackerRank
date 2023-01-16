import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    mod_dict = {}
    for i in range(k):
        mod_dict[i] = 0
    for a in s:
        mod_dict[a % k] += 1

    max_size = 0
    for i in range(k // 2 + 1):
        if i == 0:
            max_size += min(1, mod_dict[i])
        elif i == k / 2 and k % 2 == 0:
            max_size += min(1, mod_dict[i])
        else:
            max_size += max(mod_dict[i], mod_dict[k - i])
    return max_size


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()