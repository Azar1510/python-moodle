
Find the Factor
Determine the factors of a number (i.e., all positive integer values that evenly divide into a number) and then return the pth element of the list, sorted ascending. If there is no pth element, return 0.
Constraints
1 ≤ n ≤ 1015
1 ≤ p ≤ 109
The first line contains an integer n, the number to factor.
The second line contains an integer p, the 1-based index of the factor to return.

Sample Case 0
Sample Input 0
10
3
Sample Output 0
5

import sys
import math
 
def find_factors(n):
	factors = []
	for i in range(1, int(math.sqrt(n)) + 1):
    	if n % i == 0:
        	factors.append(i)
        	if i != n // i:
            	factors.append(n // i)
	return sorted(factors)
 
def get_pth_factor(n, p):
	factors = find_factors(n)
	if p <= len(factors):
    	return factors[p - 1]
	else:
    	return 0
 
# Reading input directly from the standard input (typically for competitive programming)
input = sys.stdin.read
data = input().split()
n = int(data[0])
p = int(data[1])
 
# Calculate and print the p-th factor
print(get_pth_factor(n, p))
