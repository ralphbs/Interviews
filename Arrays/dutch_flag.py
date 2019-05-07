# Write a program that takes an array A and an index into A,
# rearranges the elements such that all elements less than A[i]
# (the "pivot") appear first, followed by elements equal to the
# pivot, followed by elements greater than the pivot.

# O(n^2) solution

def dutch_flag_partition(A, pivot_index):
	pivot = A[pivot_index]
	# arrange elements less than pivot
	for i in range(len(A)):
		for j in range(i+1, len(A)):
			if A[j] < pivot:
				A[i], A[j] = A[j], A[i]
				break

	# arrange elements greater than pivot
	for i in reversed(range(len(A))):
		if A[i] < pivot:
			break
		for j in reversed(range(i)):
			if A[j] > pivot:
				A[i], A[j] = A[j], A[i]
				break
	return A

# O(n) solution with double passes

def optimized_flag_partition(A, pivot_index):
	pivot = A[pivot_index]
	smaller = 0
	# arrange elements less than pivot
	for i in range(len(A)):
		if A[i] < pivot:
			A[smaller], A[i] = A[i], A[smaller]
			smaller += 1

	# arrange elements greater than pivot
	larger = len(A) - 1
	for i in reversed(range(len(A))):
		# break because array is arranged correctly
		if A[i] < pivot:
			break
		if A[i] > pivot:
			A[larger], A[i] = A[larger], A[i]
			larger -= 1

	return A

# O(n) solution with a single pass

def very_optimized_flag_partition(A, pivot_index):
	smaller, equal, larger = 0, 0, len(A)
	pivot = A[pivot_index]
	while equal < larger:
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller+1, equal+1
		elif A[equal] == pivot:
			equal += 1
		else:
			larger -= 1
			A[larger], A[equal] = A[equal], A[larger]


def main():
	A = [5, 10, 6, 8, 2, 3, 10, 1, 0]


	# print dutch_flag_partition(A, 5)
	# print optimized_flag_partition(A, 5)
	print A
	print very_optimized_dutch_flag_partition(A, 5)	

if __name__ == '__main__':
	main()
