def is_even(num):
	if (num%2 == 0):
		return True
	return False

# Input: array of numbers
# Output: same array with even entries appearing first
def even_odd(A):
	if A is None:
		raise ValueError('The array cannot be None.')
	even_idx = 0
	odd_idx = len(A)-1
	while(even_idx<odd_idx):
		if (is_even(A[even_idx])):
			even_idx += 1
		else:
			A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
			odd_idx -= 1

	return A

def main():
	print even_odd([3, 5, 4, 7, 8, 1, 2])

if __name__ == '__main__':
	main()
