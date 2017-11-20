"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple(n, of):
	if n % of == 0:
		return True

	return False

s = 0

for i in range(1000):
	if(is_multiple(i, 3) or is_multiple(i, 5)):
		s += i

print(s)
	