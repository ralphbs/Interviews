# [2, 3, 5, 5,5,5,5, 7, 11, 11, 11, 13]
# [2, 3, 5, 7, 11, 13, 0, 0, 0]

# O(n) solution and O(1) space

# Input: a sorted array
# Output: sorted array with duplicates removed

def delete_duplicates(A):
	if A is None or len(A) == 0:
		return 0

	if len(A) == 1:
		return 1
		
	write_index = 1	
	for i in range(1, len(A)):
		if A[write_index-1] != A[i]:
			A[write_index] = A[i]
			write_index += 1
	return write_index

def main():
	print delete_duplicates([2,3,5,5,7,11,11,13, 13, 13, 13])

main()