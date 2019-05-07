# O(n) runtime, O(1) space

def plus_one(A):
	if A is None or len(A) == 0:
		raise Exception('Invalid array.')
	A[-1] += 1
	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i-1] += 1

	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A

def main():
	A = [1,0,0,1]
	print plus_one(A)

if __name__ == '__main__':
	main()